from pathlib import Path
import base64
import io
from PIL import Image

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

PARTS = Path('.source/realistic_parts')
TILE = 192
OUT = 768

for sheet_index in range(3):
    chunk_files = sorted(PARTS.glob(f's{sheet_index}_*.b64'))
    if not chunk_files:
        raise RuntimeError(f'No source chunks for sheet {sheet_index}')
    raw = b''.join(base64.b64decode(p.read_text().strip()) for p in chunk_files)
    sheet = Image.open(io.BytesIO(raw)).convert('RGB')
    if sheet.size != (576, 576):
        raise RuntimeError(f'Unexpected sheet size {sheet.size} for sheet {sheet_index}')
    for local_index in range(9):
        global_index = sheet_index * 9 + local_index
        if global_index >= len(NAMES):
            break
        x = (local_index % 3) * TILE
        y = (local_index // 3) * TILE
        tile = sheet.crop((x, y, x + TILE, y + TILE))
        tile = tile.resize((OUT, OUT), Image.Resampling.LANCZOS)
        tile.save(NAMES[global_index], 'JPEG', quality=92, subsampling=0, optimize=True, progressive=True)

print(f'Built {len(NAMES)} realistic JPG cards')
