from PIL import Image, ImageFile
from pathlib import Path

ImageFile.LOAD_TRUNCATED_IMAGES = True

NAMES = [
    'hot_chocolate.jpg',
    'lemonade_blue_curacao.jpg',
    'lemonade_citrus_mix.jpg',
    'lemonade_cola.jpg',
    'lemonade_lemon_basil.jpg',
    'lemonade_mango_passionfruit.jpg',
    'lemonade_mojito.jpg',
    'lemonade_raspberry.jpg',
    'lemonade_watermelon.jpg',
    'matcha.jpg',
    'milkshake_banana.jpg',
    'milkshake_chocolate.jpg',
    'milkshake_coconut.jpg',
    'milkshake_oreo.jpg',
    'milkshake_snickers.jpg',
    'milkshake_strawberry.jpg',
    'milkshake_vanilla_cheesecake.jpg',
    'milkshake_vanilla_classic.jpg',
    'smoothie_green_energy.jpg',
    'smoothie_strawberry_banana.jpg',
    'tea_black.jpg',
    'tea_black_sea_buckthorn.jpg',
    'tea_earl_grey.jpg',
    'tea_green_oolong.jpg',
    'tea_mulled_wine.jpg',
    'tea_raspberry_mint.jpg',
    'tea_taiga_blend.jpg',
]

SHEET = Path('.source/realistic_contact.jpg')
COLS = 5
TILE = 288
OUT = 768

sheet = Image.open(SHEET).convert('RGB')
for i, name in enumerate(NAMES):
    x = (i % COLS) * TILE
    y = (i // COLS) * TILE
    tile = sheet.crop((x, y, x + TILE, y + TILE))
    tile = tile.resize((OUT, OUT), Image.Resampling.LANCZOS)
    tile.save(name, 'JPEG', quality=92, subsampling=0, optimize=True)

print(f'Wrote {len(NAMES)} realistic JPG cards')
