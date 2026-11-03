# -*- coding: utf-8 -*-
"""
Blockout de QueNivelMaribel generado a partir del layout 2D (sketch).

Crea una malla real (Static Mesh) por pieza con Geometry Script, la guarda en
/Game/Blockout/QueNivelMaribel/ y la coloca en un nivel nuevo
/Game/Blockout/Lvl_Blockout_Maribel. Todas las piezas tienen escala 1,1,1 y las
medidas reales en la geometria, asi que se pueden editar con el Modeling Mode.

Ejecutar en Unreal (Output Log en modo Cmd):
    py "D:/QueNivelMaribel/QueNivelMaribel/Content/Python/blockout_maribel.py"

Para regenerar: borra la carpeta /Game/Blockout/QueNivelMaribel (o pon
OVERWRITE = True) y vuelve a lanzarlo.
"""

# ============================================================================
# DATOS DEL LAYOUT  (coordenadas en pixeles del sketch de 1050 x 1500)
#   - x del sketch  -> +Y de Unreal (derecha)
#   - y del sketch  -> -X de Unreal (arriba del sketch = +X, "norte")
#   - Origen (0,0,0) = centro del sketch
# ============================================================================
# --- LAYOUT_BEGIN ---
CM_PER_PX = 4.0           # 1 px = 4 cm  ->  zona de ~42 x 60 m
ORIGIN_PX = (525.0, 750.0)

# Alturas (cm)
FLOOR_THICKNESS = 100.0
H_MESETA_ALTA = 600.0      # mesetas del norte (unidas por el tronco de arriba)
H_MESETA_ESTE = 350.0      # meseta del este (sale el tronco diagonal)
H_PERIMETRO = 1600.0       # paredes de roca que cierran la zona
PERIM_THICK = 400.0
ABISMO_Z = -1500.0         # fondo de las grietas

# Contorno interior del suelo (el rectangulo de roca del sketch)
SUELO = [(45, 35), (1020, 45), (1000, 1470), (110, 1478)]

# Piezas extruidas: nombre, poligono (px), z base (cm), altura (cm)
EXTRUSIONES = [
    ("Meseta_NO", [(45, 40), (170, 38), (210, 70), (240, 190), (275, 265),
                   (320, 300), (335, 345), (305, 385), (250, 402), (150, 378),
                   (45, 350)], 0.0, H_MESETA_ALTA),
    ("Meseta_NE", [(770, 90), (870, 48), (1018, 45), (1016, 330), (840, 332),
                   (745, 302), (708, 255), (735, 175)], 0.0, H_MESETA_ALTA),
    ("Meseta_E", [(700, 352), (760, 338), (850, 342), (1015, 345), (1012, 640),
                  (965, 625), (905, 690), (860, 640), (790, 525), (705, 480),
                  (682, 420)], 0.0, H_MESETA_ESTE),
    ("Roca_Escalon_O", [(240, 468), (342, 440), (372, 452), (390, 498),
                        (368, 522), (262, 532), (240, 495)], 0.0, 150.0),
    ("Losa_Flecha", [(440, 925), (530, 882), (600, 892), (702, 1062),
                     (688, 1086), (600, 1090), (556, 1042), (528, 1052),
                     (518, 1000), (470, 982)], 0.0, 120.0),
    ("Roca_Grande", [(690, 880), (740, 842), (812, 842), (850, 900), (860, 982),
                     (820, 1052), (740, 1062), (680, 1032), (655, 965)],
     0.0, 380.0),
]

# Grietas: se restan del suelo (boolean) y dejan ver el abismo
GRIETAS = [
    ("Grieta_Central", [(250, 195), (380, 190), (390, 300), (400, 440),
                        (420, 520), (440, 600), (420, 660), (352, 722),
                        (372, 822), (396, 932), (422, 1022), (390, 962),
                        (330, 850), (300, 760), (320, 640), (300, 590),
                        (330, 560), (378, 470), (340, 382), (320, 320)]),
    ("Grieta_Este", [(680, 440), (702, 482), (694, 560), (694, 700),
                     (724, 778), (754, 834), (734, 842), (700, 792),
                     (672, 722), (668, 560)]),
    ("Grieta_SO", [(285, 772), (300, 790), (218, 872), (150, 962),
                   (128, 972), (200, 860)]),
]

# Muro curvo del sur (cuenca en U): polilinea + grosor (px) + altura (cm)
MURO_U = ("Muro_Cuenca_U",
          [(410, 1102), (362, 1140), (342, 1210), (348, 1268), (385, 1320),
           (460, 1358), (560, 1384), (650, 1388), (745, 1366), (820, 1320),
           (865, 1255), (880, 1195), (870, 1142)], 22.0, 160.0)

# Troncos: nombre, extremo A (px, z cm), extremo B (px, z cm), radio (cm)
TRONCOS = [
    ("Tronco_Puente_N", (125, 136, H_MESETA_ALTA), (742, 178, H_MESETA_ALTA),
     150.0),
    ("Tronco_Rampa_Diagonal", (775, 498, H_MESETA_ESTE), (228, 738, 0.0),
     130.0),
]

# Piedras pequenas / pilotes: nombre, centro px, tamano px (w,l), yaw deg, alto cm
POSTES = [
    ("Pilote_01", (240, 896), (18, 40), -15.0, 80.0),
    ("Pilote_02", (235, 976), (18, 40), -15.0, 80.0),
    ("Pilote_03", (295, 990), (18, 40), -15.0, 80.0),
    ("Pilote_04", (290, 1072), (18, 40), -15.0, 80.0),
]
PIEDRAS = [  # nombre, centro px, radio cm, alto cm
    ("Piedra_SE_01", (858, 1330), 55.0, 80.0),
    ("Piedra_SE_02", (845, 1376), 45.0, 60.0),
    ("Marcador_Corazon", (505, 790), 70.0, 40.0),
]

PLAYER_START_PX = (600, 1300)
# --- LAYOUT_END ---

# ============================================================================
import math
import unreal

ASSET_DIR = "/Game/Blockout/QueNivelMaribel"
LEVEL_PATH = "/Game/Blockout/Lvl_Blockout_Maribel"
MATERIAL = "/Game/LevelPrototyping/Materials/MI_PrototypeGrid_Gray"
MATERIAL_ALT = "/Game/LevelPrototyping/Materials/MI_PrototypeGrid_TopDark"
OVERWRITE = True
FLIP_WINDING = False   # si alguna pieza sale "del reves", cambia esto a True

log = unreal.log


def px2cm(p):
    x, y = p
    return ((ORIGIN_PX[1] - y) * CM_PER_PX, (x - ORIGIN_PX[0]) * CM_PER_PX)


def signed_area(pts):
    a = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        a += x1 * y2 - x2 * y1
    return a * 0.5


def centroid(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return ((min(xs) + max(xs)) * 0.5, (min(ys) + max(ys)) * 0.5)


def prep_poly(pts_cm, center):
    """Poligono local (relativo al pivote) con winding consistente."""
    local = [(p[0] - center[0], p[1] - center[1]) for p in pts_cm]
    ccw = signed_area(local) > 0
    if ccw == FLIP_WINDING:
        local = list(reversed(local))
    return [unreal.Vector2D(x, y) for x, y in local]


def new_mesh():
    return unreal.DynamicMesh()


OPTS = unreal.GeometryScriptPrimitiveOptions()


def identity():
    return unreal.Transform()


def append_extrude(mesh, poly_v2, z0, height):
    t = unreal.Transform(location=unreal.Vector(0, 0, z0))
    unreal.GeometryScript_Primitives.append_simple_extrude_polygon(
        mesh, OPTS, t, poly_v2, height, 0, True)


def finish_mesh(mesh):
    try:
        unreal.GeometryScript_Normals.compute_split_normals(
            mesh, unreal.GeometryScriptSplitNormalsOptions(),
            unreal.GeometryScriptCalculateNormalsOptions())
    except Exception as e:  # noqa
        log("normals: %s" % e)
    try:
        box = unreal.Transform(scale=unreal.Vector(100, 100, 100))
        unreal.GeometryScript_UVs.set_mesh_u_vs_from_box_projection(
            mesh, 0, box, unreal.GeometryScriptMeshSelection(), 2)
    except Exception as e:  # noqa
        log("uvs: %s" % e)


def save_mesh(mesh, name):
    path = "%s/%s" % (ASSET_DIR, name)
    if unreal.EditorAssetLibrary.does_asset_exist(path):
        if OVERWRITE:
            unreal.EditorAssetLibrary.delete_asset(path)
        else:
            return unreal.EditorAssetLibrary.load_asset(path)
    opts = unreal.GeometryScriptCreateNewStaticMeshAssetOptions()
    for k, v in (("enable_recompute_normals", False),
                 ("enable_recompute_tangents", True),
                 ("enable_nanite", False),
                 ("enable_collision", True),
                 ("collision_mode", unreal.CollisionTraceFlag.CTF_USE_COMPLEX_AS_SIMPLE)):
        try:
            opts.set_editor_property(k, v)
        except Exception as e:  # noqa
            log("opcion %s: %s" % (k, e))
    res = unreal.GeometryScript_NewAssetUtils.create_new_static_mesh_asset_from_mesh(
        mesh, path, opts)
    sm = None
    for r in (res if isinstance(res, tuple) else (res,)):
        if isinstance(r, unreal.StaticMesh):
            sm = r
    if sm is None:
        sm = unreal.EditorAssetLibrary.load_asset(path)
    mat = unreal.EditorAssetLibrary.load_asset(
        MATERIAL_ALT if name.startswith(("Tronco", "Pilote", "Piedra", "Marcador"))
        else MATERIAL)
    if sm and mat:
        sm.set_material(0, mat)
    unreal.EditorAssetLibrary.save_asset(path, only_if_is_dirty=False)
    return sm


ACTORS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)


def place(sm, name, loc_xy, z=0.0, folder="Blockout"):
    a = ACTORS.spawn_actor_from_object(sm, unreal.Vector(loc_xy[0], loc_xy[1], z))
    a.set_actor_label(name)
    a.set_folder_path(folder)
    return a


def build_extrusion(name, pts_px, z0, height, folder, cut=None):
    pts = [px2cm(p) for p in pts_px]
    c = centroid(pts)
    mesh = new_mesh()
    append_extrude(mesh, prep_poly(pts, c), z0, height)
    for cpts_px in (cut or []):
        tool = new_mesh()
        cpts = [px2cm(p) for p in cpts_px]
        append_extrude(tool, prep_poly(cpts, c), z0 - 200, height + 400)
        unreal.GeometryScript_MeshBooleans.apply_mesh_boolean(
            mesh, identity(), tool, identity(),
            unreal.GeometryScriptBooleanOperation.SUBTRACT,
            unreal.GeometryScriptMeshBooleanOptions())
    finish_mesh(mesh)
    place(save_mesh(mesh, name), name, c, 0.0, folder)


def strip_from_polyline(pts, half_w):
    """Convierte una polilinea en un poligono con grosor."""
    left, right = [], []
    n = len(pts)
    for i in range(n):
        p0 = pts[max(i - 1, 0)]
        p1 = pts[min(i + 1, n - 1)]
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        left.append((pts[i][0] + nx * half_w, pts[i][1] + ny * half_w))
        right.append((pts[i][0] - nx * half_w, pts[i][1] - ny * half_w))
    return left + list(reversed(right))


def build_log(name, a, b, radius):
    pa = px2cm(a[:2]) + (a[2] + radius * 0.55,)
    pb = px2cm(b[:2]) + (b[2] + radius * 0.55,)
    mid = tuple((pa[i] + pb[i]) * 0.5 for i in range(3))
    d = unreal.Vector(pb[0] - pa[0], pb[1] - pa[1], pb[2] - pa[2])
    length = d.length()
    rot = unreal.MathLibrary.make_rot_from_z(d)
    start = unreal.Vector(pa[0] - mid[0], pa[1] - mid[1], pa[2] - mid[2])
    mesh = new_mesh()
    unreal.GeometryScript_Primitives.append_cylinder(
        mesh, OPTS, unreal.Transform(location=start, rotation=rot),
        radius, length, 16, 0, True,
        unreal.GeometryScriptPrimitiveOriginMode.BASE)
    finish_mesh(mesh)
    place(save_mesh(mesh, name), name, mid[:2], mid[2], "Blockout/Troncos")


def build_box(name, c_px, size_px, yaw, h):
    c = px2cm(c_px)
    mesh = new_mesh()
    unreal.GeometryScript_Primitives.append_box(
        mesh, OPTS,
        unreal.Transform(rotation=unreal.Rotator(0, 0, -yaw)),
        size_px[1] * CM_PER_PX, size_px[0] * CM_PER_PX, h, 0, 0, 0,
        unreal.GeometryScriptPrimitiveOriginMode.BASE)
    finish_mesh(mesh)
    place(save_mesh(mesh, name), name, c, 0.0, "Blockout/Detalles")


def build_rock(name, c_px, r, h):
    c = px2cm(c_px)
    mesh = new_mesh()
    unreal.GeometryScript_Primitives.append_cylinder(
        mesh, OPTS, identity(), r, h, 7, 0, True,
        unreal.GeometryScriptPrimitiveOriginMode.BASE)
    finish_mesh(mesh)
    place(save_mesh(mesh, name), name, c, 0.0, "Blockout/Detalles")


def build_perimeter():
    pts = [px2cm(p) for p in SUELO]
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    names = ["Muro_Perimetro_N", "Muro_Perimetro_E",
             "Muro_Perimetro_S", "Muro_Perimetro_O"]
    for i in range(4):
        p0, p1 = pts[i], pts[(i + 1) % 4]
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        if (mx - cx) * nx + (my - cy) * ny < 0:   # normal hacia fuera
            nx, ny = -nx, -ny
        ext = PERIM_THICK
        quad = [(p0[0] - dx / L * ext, p0[1] - dy / L * ext),
                (p1[0] + dx / L * ext, p1[1] + dy / L * ext),
                (p1[0] + dx / L * ext + nx * ext, p1[1] + dy / L * ext + ny * ext),
                (p0[0] - dx / L * ext + nx * ext, p0[1] - dy / L * ext + ny * ext)]
        c = centroid(quad)
        mesh = new_mesh()
        append_extrude(mesh, prep_poly(quad, c), ABISMO_Z, H_PERIMETRO - ABISMO_Z)
        finish_mesh(mesh)
        place(save_mesh(mesh, names[i]), names[i], c, 0.0, "Blockout/Perimetro")


def build_lighting():
    E = ACTORS
    sun = E.spawn_actor_from_class(unreal.DirectionalLight, unreal.Vector(0, 0, 3000),
                                   unreal.Rotator(0, -50, -35))
    sun.set_actor_label("Sol")
    sun.light_component.set_editor_property("atmosphere_sun_light", True)
    sun.light_component.set_editor_property("intensity", 8.0)
    sky = E.spawn_actor_from_class(unreal.SkyLight, unreal.Vector(0, 0, 3200))
    sky.set_actor_label("SkyLight")
    sky.light_component.set_editor_property("real_time_capture", True)
    sky.light_component.set_editor_property("mobility", unreal.ComponentMobility.MOVABLE)
    E.spawn_actor_from_class(unreal.SkyAtmosphere, unreal.Vector(0, 0, 0)).set_actor_label("SkyAtmosphere")
    E.spawn_actor_from_class(unreal.ExponentialHeightFog, unreal.Vector(0, 0, -800)).set_actor_label("Niebla")
    for a in E.get_all_level_actors():
        if a.get_actor_label() in ("Sol", "SkyLight", "SkyAtmosphere", "Niebla"):
            a.set_folder_path("Iluminacion")
    ps = E.spawn_actor_from_class(unreal.PlayerStart,
                                  unreal.Vector(*(px2cm(PLAYER_START_PX) + (120.0,))),
                                  unreal.Rotator(0, 0, 0))
    ps.set_folder_path("Gameplay")


def main():
    les = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    if unreal.EditorAssetLibrary.does_asset_exist(LEVEL_PATH):
        les.load_level(LEVEL_PATH)
        for a in ACTORS.get_all_level_actors():
            ACTORS.destroy_actor(a)
    else:
        les.new_level(LEVEL_PATH)

    with unreal.ScopedSlowTask(20, "Blockout QueNivelMaribel") as task:
        task.make_dialog(True)
        task.enter_progress_frame(1, "Suelo")
        build_extrusion("Suelo_Base", SUELO, -FLOOR_THICKNESS, FLOOR_THICKNESS,
                        "Blockout/Suelo", cut=[g[1] for g in GRIETAS])
        # Fondo del abismo bajo las grietas
        build_extrusion("Abismo_Fondo", SUELO, ABISMO_Z - 100, 100, "Blockout/Suelo")
        task.enter_progress_frame(1, "Perimetro")
        build_perimeter()
        for name, pts, z0, h in EXTRUSIONES:
            task.enter_progress_frame(1, name)
            folder = "Blockout/Mesetas" if name.startswith("Meseta") else "Blockout/Rocas"
            build_extrusion(name, pts, z0, h, folder)
        task.enter_progress_frame(1, "Muro U")
        n, line, w, h = MURO_U
        build_extrusion(n, strip_from_polyline(line, w * 0.5), 0.0, h, "Blockout/Rocas")
        for name, a, b, r in TRONCOS:
            task.enter_progress_frame(1, name)
            build_log(name, a, b, r)
        for name, c, s, yaw, h in POSTES:
            build_box(name, c, s, yaw, h)
        for name, c, r, h in PIEDRAS:
            build_rock(name, c, r, h)
        build_lighting()

    les.save_current_level()
    log("Blockout QueNivelMaribel terminado")


main()
