# -*- coding: utf-8 -*-
"""
Blockout del CAMPAMENTO de QueNivelMaribel (segunda zona), a partir del layout 2D.

Mismo sistema que blockout_maribel.py: una Static Mesh real por pieza (Geometry
Script), escala 1,1,1, pivote en la base, editable con el Modeling Mode.
Assets en /Game/Blockout/Campamento/ y actores en la carpeta "Campamento" del
Outliner de /Game/Blockout/Lvl_Blockout_Maribel.

Ejecutar (Output Log, modo Cmd):
    py "D:/QueNivelMaribel/QueNivelMaribel/Content/Python/blockout_campamento.py"
Al relanzarlo solo se borra y regenera lo que esta en la carpeta "Campamento".
"""

# --- LAYOUT_BEGIN ---
# Coordenadas sobre el sketch reducido a 2000 x 1500 px.  x -> +Y (derecha), y -> -X (arriba = norte)
CM_PER_PX = 5.0                 # 1 px = 5 cm -> campamento de ~80 x 72 m
# El punto del sketch ANCLA_PX cae en ANCLA_UE (cm). Por defecto la salida sur
# del campamento queda centrada justo al norte de la primera zona.
ANCLA_PX = (1135.0, 1440.0)
ANCLA_UE = (3260.0, 0.0)

H_EMPALIZADA = 400.0
G_EMPALIZADA = 12.0             # grosor en px (60 cm)

SUELO = [(405, 0), (2000, 0), (2000, 1445), (360, 1445)]

# Caminos: losa fina con material oscuro para que se lean
CAMINOS = [
    ("Camino_Edificio_Este", [(942, 75), (1090, 70), (1105, 150), (1390, 155),
                              (1400, 260), (1100, 250), (1085, 372), (715, 358),
                              (710, 300), (942, 298)]),
    ("Camino_Norte_Este", [(1380, 0), (1482, 0), (1480, 380), (1490, 410),
                           (1540, 430), (2000, 465), (2000, 575), (1380, 575)]),
    ("Camino_Sur", [(1112, 632), (1245, 642), (1215, 1060), (1222, 1445),
                    (1030, 1445), (1028, 1075), (720, 1075), (715, 962),
                    (1090, 962)]),
]

# Volumenes: nombre, poligono (px), altura (cm), subcarpeta
VOLUMENES = [
    ("Edificio_Principal", [(555, 82), (940, 92), (942, 295), (552, 283)], 500.0, "Edificios"),
    ("Edificio_SO", [(445, 970), (697, 975), (697, 1272), (445, 1272)], 600.0, "Edificios"),
    ("Edificio_SE_01", [(1302, 1205), (1538, 1222), (1528, 1345), (1308, 1360)], 500.0, "Edificios"),
    ("Edificio_SE_02", [(1615, 1082), (1782, 1080), (1802, 1335), (1622, 1338)], 700.0, "Edificios"),
    ("Bloque_NE_Esquina", [(1670, 0), (2000, 0), (2000, 202), (1680, 197), (1662, 172)], 400.0, "Terreno"),
    ("Bloque_NE", [(1662, 207), (2000, 207), (2000, 460), (1545, 430), (1500, 405), (1575, 340)], 300.0, "Terreno"),
    ("Plataforma_Central", [(617, 452), (940, 450), (937, 578), (620, 582)], 60.0, "Props"),
    ("Tienda_Mastil", [(1008, 425), (1090, 428), (1105, 505), (1022, 530)], 350.0, "Tiendas"),
]

# Cajas rectangulares: nombre, (x0, y0, x1, y1) px, altura cm, subcarpeta
CAJAS = [
    ("Tienda_O_01", (398, 403, 442, 468), 250.0, "Tiendas"),
    ("Tienda_O_02", (380, 487, 440, 560), 250.0, "Tiendas"),
    ("Carro_01", (415, 603, 545, 690), 200.0, "Props"),
    ("Carro_02", (415, 755, 535, 848), 200.0, "Props"),
    ("Tienda_C_01", (790, 643, 858, 715), 300.0, "Tiendas"),
    ("Tienda_C_02", (645, 742, 712, 825), 300.0, "Tiendas"),
    ("Tienda_C_03", (800, 752, 897, 842), 300.0, "Tiendas"),
    ("Tienda_C_04", (967, 750, 1042, 832), 300.0, "Tiendas"),
    ("Tienda_E_01", (1230, 290, 1317, 352), 300.0, "Tiendas"),
    ("Tienda_E_02", (1198, 360, 1315, 448), 300.0, "Tiendas"),
    ("Tienda_E_03", (1205, 475, 1310, 560), 300.0, "Tiendas"),
    ("Tienda_SE_01", (1368, 635, 1470, 720), 300.0, "Tiendas"),
    ("Tienda_SE_02", (1570, 635, 1675, 720), 300.0, "Tiendas"),
    ("Tienda_SE_03", (1370, 782, 1477, 880), 300.0, "Tiendas"),
    ("Tienda_SE_04", (1555, 805, 1682, 890), 300.0, "Tiendas"),
    ("Tienda_SE_05", (1328, 940, 1490, 1035), 300.0, "Tiendas"),
    ("Tienda_SE_06", (1580, 935, 1697, 1033), 300.0, "Tiendas"),
    ("Escalera_Edificio", (605, 292, 650, 300), 500.0, "Edificios"),
]

# Muros finos sobre polilineas: nombre, puntos px, grosor px, altura cm
MUROS = [
    ("Empalizada_O", [(405, 0), (383, 700), (360, 1445)], G_EMPALIZADA, H_EMPALIZADA),
    ("Empalizada_S_01", [(530, 1432), (985, 1438)], G_EMPALIZADA, H_EMPALIZADA),
    ("Empalizada_S_02", [(1310, 1432), (1945, 1445)], G_EMPALIZADA, H_EMPALIZADA),
    ("Valla_Diagonal_01", [(1575, 340), (1650, 210)], 8.0, 150.0),
    ("Valla_Diagonal_02", [(1710, 165), (1835, 30)], 8.0, 150.0),
]

# Cilindros: nombre, centro px, radio cm, altura cm, subcarpeta
CILINDROS = [
    ("Hoguera_Campamento", (990, 667), 100.0, 40.0, "Props"),
    ("Prop_Roca_Plataforma", (728, 512), 150.0, 120.0, "Props"),
    ("Mastil", (1040, 400), 15.0, 700.0, "Props"),
    ("Marcador_Humo_O", (300, 470), 120.0, 60.0, "Props"),
]
# --- LAYOUT_END ---

import math
import traceback
import unreal

ASSET_DIR = "/Game/Blockout/Campamento"
LEVEL_PATH = "/Game/Blockout/Lvl_Blockout_Maribel"
ROOT = "Campamento"
MAT_DEFAULT = "/Game/LevelPrototyping/Materials/MI_PrototypeGrid_Gray"
MAT_DARK = "/Game/LevelPrototyping/Materials/MI_PrototypeGrid_TopDark"
MAT_ALT = "/Game/LevelPrototyping/Materials/MI_PrototypeGrid_Gray_02"

ACTORS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
OPTS = unreal.GeometryScriptPrimitiveOptions()


def px2cm(p):
    return (ANCLA_UE[0] + (ANCLA_PX[1] - p[1]) * CM_PER_PX,
            ANCLA_UE[1] + (p[0] - ANCLA_PX[0]) * CM_PER_PX)


def signed_area(pts):
    return 0.5 * sum(pts[i][0] * pts[(i + 1) % len(pts)][1] -
                     pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))


def centroid(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return ((min(xs) + max(xs)) * 0.5, (min(ys) + max(ys)) * 0.5)


def local_poly(pts_cm, c):
    loc = [(p[0] - c[0], p[1] - c[1]) for p in pts_cm]
    if signed_area(loc) < 0:          # Geometry Script quiere CCW
        loc.reverse()
    return [unreal.Vector2D(x, y) for x, y in loc]


def finish(mesh):
    try:
        unreal.GeometryScript_Normals.compute_split_normals(
            mesh, unreal.GeometryScriptSplitNormalsOptions(),
            unreal.GeometryScriptCalculateNormalsOptions())
    except Exception as e:  # noqa
        unreal.log_warning("normals: %s" % e)
    try:
        unreal.GeometryScript_UVs.set_mesh_u_vs_from_box_projection(
            mesh, 0, unreal.Transform(scale=unreal.Vector(100, 100, 100)),
            unreal.GeometryScriptMeshSelection(), 2)
    except Exception as e:  # noqa
        unreal.log_warning("uvs: %s" % e)


def save(mesh, name, material):
    path = "%s/%s" % (ASSET_DIR, name)
    if unreal.EditorAssetLibrary.does_asset_exist(path):
        unreal.EditorAssetLibrary.delete_asset(path)
    o = unreal.GeometryScriptCreateNewStaticMeshAssetOptions()
    for k, v in (("enable_recompute_normals", False),
                 ("enable_recompute_tangents", True),
                 ("enable_nanite", False),
                 ("enable_collision", True),
                 ("collision_mode", unreal.CollisionTraceFlag.CTF_USE_COMPLEX_AS_SIMPLE)):
        try:
            o.set_editor_property(k, v)
        except Exception as e:  # noqa
            unreal.log_warning("opcion %s: %s" % (k, e))
    res = unreal.GeometryScript_NewAssetUtils.create_new_static_mesh_asset_from_mesh(mesh, path, o)
    sm = None
    for r in (res if isinstance(res, tuple) else (res,)):
        if isinstance(r, unreal.StaticMesh):
            sm = r
    sm = sm or unreal.EditorAssetLibrary.load_asset(path)
    mat = unreal.EditorAssetLibrary.load_asset(material)
    if sm and mat:
        sm.set_material(0, mat)
    unreal.EditorAssetLibrary.save_asset(path, only_if_is_dirty=False)
    return sm


def place(sm, name, xy, folder):
    a = ACTORS.spawn_actor_from_object(sm, unreal.Vector(xy[0], xy[1], 0.0))
    a.set_actor_label(name)
    a.set_folder_path("%s/%s" % (ROOT, folder))


def extrude(name, pts_px, z0, h, folder, material=MAT_DEFAULT):
    pts = [px2cm(p) for p in pts_px]
    c = centroid(pts)
    mesh = unreal.DynamicMesh()
    unreal.GeometryScript_Primitives.append_simple_extrude_polygon(
        mesh, OPTS, unreal.Transform(location=unreal.Vector(0, 0, z0)),
        local_poly(pts, c), h, 0, True)
    finish(mesh)
    place(save(mesh, name, material), name, c, folder)


def rect(r):
    x0, y0, x1, y1 = r
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def strip(pts, half_w):
    left, right = [], []
    n = len(pts)
    for i in range(n):
        p0, p1 = pts[max(i - 1, 0)], pts[min(i + 1, n - 1)]
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        left.append((pts[i][0] + nx * half_w, pts[i][1] + ny * half_w))
        right.append((pts[i][0] - nx * half_w, pts[i][1] - ny * half_w))
    return left + right[::-1]


def cylinder(name, c_px, r, h, folder):
    c = px2cm(c_px)
    mesh = unreal.DynamicMesh()
    unreal.GeometryScript_Primitives.append_cylinder(
        mesh, OPTS, unreal.Transform(), r, h, 12, 0, True,
        unreal.GeometryScriptPrimitiveOriginMode.BASE)
    finish(mesh)
    place(save(mesh, name, MAT_ALT), name, c, folder)


def clear_previous():
    les = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()
    if not world or world.get_path_name().split(".")[0] != LEVEL_PATH:
        les.load_level(LEVEL_PATH)
    for a in ACTORS.get_all_level_actors():
        if str(a.get_folder_path()).startswith(ROOT):
            ACTORS.destroy_actor(a)
    return les


def main():
    les = clear_previous()
    total = 2 + len(CAMINOS) + len(VOLUMENES) + len(CAJAS) + len(MUROS) + len(CILINDROS)
    with unreal.ScopedSlowTask(total, "Blockout Campamento") as task:
        task.make_dialog(True)
        task.enter_progress_frame(1, "Suelo")
        extrude("Suelo_Campamento", SUELO, -100.0, 100.0, "Suelo")
        for n, pts in CAMINOS:
            task.enter_progress_frame(1, n)
            extrude(n, pts, 0.0, 3.0, "Caminos", MAT_DARK)
        for n, pts, h, f in VOLUMENES:
            task.enter_progress_frame(1, n)
            extrude(n, pts, 0.0, h, f)
        for n, r, h, f in CAJAS:
            task.enter_progress_frame(1, n)
            extrude(n, rect(r), 0.0, h, f, MAT_ALT if f == "Tiendas" else MAT_DEFAULT)
        for n, line, w, h in MUROS:
            task.enter_progress_frame(1, n)
            extrude(n, strip(line, w * 0.5), 0.0, h, "Muros")
        for n, c, r, h, f in CILINDROS:
            task.enter_progress_frame(1, n)
            cylinder(n, c, r, h, f)
    les.save_current_level()
    unreal.log("Blockout Campamento terminado")


_log_path = unreal.Paths.convert_relative_path_to_full(
    unreal.Paths.project_saved_dir()) + "blockout_campamento_log.txt"
try:
    main()
    open(_log_path, "w").write("OK\n")
except Exception:
    open(_log_path, "w").write(traceback.format_exc())
    raise
