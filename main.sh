cd "$(dirname "$(realpath "$0")")";

if python main.py; then
	cd public && python -m http.server 8888
fi
