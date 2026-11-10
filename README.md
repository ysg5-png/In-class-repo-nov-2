some instructions here

1. Clone [the repo](https://github.com/s2t2/my-first-app-fall-2026) from GitHub, and put it somewhere (like your Desktop).
2. Navigate to the local repo from the command line (for example if on your desktop):

```sh
cd ~/Desktop/my-first-app-fall-2026
```

3. Create a new Anaconda virtual environment called "rps-env" (first time only):

```sh
conda create -n rps-env python=3.11
```

4. Activate the virtual environment as necessary (every time you come back to the project):

```sh
conda activate rps-env
```

5. Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

# alternatively:
python -m app.rps
```

## Testing

To run tests:

```sh
pytest
```