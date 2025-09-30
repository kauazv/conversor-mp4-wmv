import os
from converter import mp4_to_wav

def main():
    print("=== Conversor MP4 → WAV ===")
    input_file = input("Digite o caminho do arquivo .mp4: ").strip()

    if not os.path.exists(input_file):
        print("[ERRO] Arquivo não encontrado.")
        return

    output_file = os.path.splitext(input_file)[0] + ".wav"
    mp4_to_wav(input_file, output_file)

if __name__ == "__main__":
    main()
