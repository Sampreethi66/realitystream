import sys
from models.run_models_core import load_parameters

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_models.py <parameters.yaml>")
        sys.exit(1)

    params_path = sys.argv[1]
    params = load_parameters(params_path)

    print("Loaded parameters:")
    print(params)

if __name__ == "__main__":
    main()
