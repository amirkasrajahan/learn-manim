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

## Frontend

`frontend/` is a React + TypeScript (Vite) app with a dropdown that plays the rendered videos.

```bash
./render.sh                 # render all scenes into frontend/public/videos/
cd frontend && npm install && npm run dev
```

To add an algorithm: write the scene in `algorithms/`, add a line to `SCENES` in `render.sh`, and add an entry to `frontend/src/algorithms.ts`.

## Rendering a scene

```bash
manim -pql <file> <SceneName>
```

Example:

```bash
manim -pql algorithms/linear_search.py LinearSearch
```

`-p` previews the video after rendering, `-ql` renders at low quality for fast iteration. Drop `-ql` (or use `-qh`) for higher quality once a scene is finished.
