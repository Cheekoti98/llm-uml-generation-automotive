import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

def load_model(base_model_name: str, lora_checkpoint_path: str | None = None):
    """
    Load base model and (optionally) attach LoRA weights.
    """
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    if lora_checkpoint_path:
        model = PeftModel.from_pretrained(model, lora_checkpoint_path)
    model.eval()
    return tokenizer, model

def extract_plantuml(text: str) -> str:
    """
    Return only the @startuml ... @enduml block if present.
    """
    m = re.search(r"@startuml.*?@enduml", text, flags=re.DOTALL)
    return m.group(0).strip() if m else text.strip()

def generate_uml(requirement: str, tokenizer, model, max_new_tokens: int = 200) -> str:
    prompt = (
        "### Instruction:\n"
        "Convert the requirement into a PlantUML class diagram. Return only PlantUML code.\n\n"
        f"### Input:\n{requirement}\n\n"
        "### Output:\n"
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False
        )
    decoded = tokenizer.decode(out[0], skip_special_tokens=True)
    return extract_plantuml(decoded)
