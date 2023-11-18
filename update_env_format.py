"""
Read env file and create a env format file with empty values
"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", "-e", type=str, help="path to env file", default=".env.local")
    parser.add_argument("--output-path", "-o", type=str, help="path to output file", default=".env-format")
    args = parser.parse_args()

    env_path = args.env
    out_path = args.output_path

    env_format_content = ""
    with open(env_path) as f:
        lines = [line.strip().split("=") for line in f.readlines() if line.strip() != ""]
        for key, _ in lines:
            env_format_content += f"{key}=\n"

    with open(out_path, "w") as f:
        f.write(env_format_content)


if __name__ == "__main__":
    main()
