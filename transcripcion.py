import whisper
from rich.console import Console
from rich.panel import Panel

console = Console()

# Cargar modelo y transcribir
model = whisper.load_model("large")
result = model.transcribe("./rod.mp3")
letra = result["text"]

# Mostrar la letra con un panel bonito
console.print(Panel(letra, title="🎶 Letra Transcrita", subtitle="Powered by Whisper + Rich", style="bold cyan"))
