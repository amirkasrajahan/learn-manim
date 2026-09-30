# learn-manim

Practice project for learning [Manim](https://docs.manim.community/) and using it to visualize data structures and algorithms.

## Structure

- `basics/` — tutorial exercises (shapes, transforms, positioning). Not DSA-related, just learning the API.
- `algorithms/` — one file per algorithm, e.g. `linear_search.py`. As more get added, they'll group naturally by topic (`algorithms/sorting/`, `algorithms/trees/`, etc.) once there's more than one per category.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Also requires `cairo`, `pkg-config`, and `ffmpeg` on the system (macOS: `brew install cairo pkg-config ffmpeg`).

## Rendering a scene

```bash
manim -pql <file> <SceneName>
```

Example:

```bash
manim -pql algorithms/linear_search.py LinearSearch
```

`-p` previews the video after rendering, `-ql` renders at low quality for fast iteration. Drop `-ql` (or use `-qh`) for higher quality once a scene is finished.
