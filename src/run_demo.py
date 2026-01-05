from src.uml_generation.generate import load_model, generate_uml

if __name__ == "__main__":
    BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    # Optional: later set this to your Drive checkpoint path if you want
    LORA_CKPT = None

    tokenizer, model = load_model(BASE_MODEL, LORA_CKPT)

    req = "The EmergencyBrakingSystem shall detect obstacles using FrontRadar and apply brakes using BrakeActuator."
    print(generate_uml(req, tokenizer, model))
