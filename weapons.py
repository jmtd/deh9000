
import c
from states import *

ammotype_t = c.Enum([
	"am_clip",    # Pistol / chaingun ammo.
	"am_shell",   # Shotgun / double barreled shotgun.
	"am_cell",    # Plasma rifle, BFG.
	"am_misl",    # Missile launcher.
	"NUMAMMO",
	"am_noammo",  # Unlimited for chainsaw / fist.
])

ammotype_t.create_globals(globals())

weapontype_t = c.Enum([
	"wp_fist",
	"wp_pistol",
	"wp_shotgun",
	"wp_chaingun",
	"wp_missile",
	"wp_plasma",
	"wp_bfg",
	"wp_chainsaw",
	"wp_supershotgun",
])

weapontype_t.create_globals(globals())

NUMWEAPONS = len(weapontype_t)

weaponinfo_t = c.Struct("weaponinfo_t", "Weapon", [
	("ammo",        "Ammo type"),
	("upstate",     "Deselect frame"),
	("downstate",   "Select frame"),
	("readystate",  "Bobbing frame"),
	("atkstate",    "Shooting frame"),
	("flashstate",  "Firing frame"),
])

weaponinfo = c.StructArray(weaponinfo_t, [
    (
        # fist
        am_noammo,
        S_PUNCHUP,
        S_PUNCHDOWN,
        S_PUNCH,
        S_PUNCH1,
        S_NULL
    ),
    (
        # pistol
        am_clip,
        S_PISTOLUP,
        S_PISTOLDOWN,
        S_PISTOL,
        S_PISTOL1,
        S_PISTOLFLASH
    ),
    (
        # shotgun
        am_shell,
        S_SGUNUP,
        S_SGUNDOWN,
        S_SGUN,
        S_SGUN1,
        S_SGUNFLASH1
    ),
    (
        # chaingun
        am_clip,
        S_CHAINUP,
        S_CHAINDOWN,
        S_CHAIN,
        S_CHAIN1,
        S_CHAINFLASH1
    ),
    (
        # missile launcher
        am_misl,
        S_MISSILEUP,
        S_MISSILEDOWN,
        S_MISSILE,
        S_MISSILE1,
        S_MISSILEFLASH1
    ),
    (
        # plasma rifle
        am_cell,
        S_PLASMAUP,
        S_PLASMADOWN,
        S_PLASMA,
        S_PLASMA1,
        S_PLASMAFLASH1
    ),
    (
        # bfg 9000
        am_cell,
        S_BFGUP,
        S_BFGDOWN,
        S_BFG,
        S_BFG1,
        S_BFGFLASH1
    ),
    (
        # chainsaw
        am_noammo,
        S_SAWUP,
        S_SAWDOWN,
        S_SAW,
        S_SAW1,
        S_NULL
    ),
    (
        # super shotgun
        am_shell,
        S_DSGUNUP,
        S_DSGUNDOWN,
        S_DSGUN,
        S_DSGUN1,
        S_DSGUNFLASH1
    ),
])

