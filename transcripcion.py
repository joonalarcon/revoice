import whisper
from rich.console import Console
from rich.panel import Panel

console = Console()

model = whisper.load_model("large")
result = model.transcribe("./rod.mp3")
letra = result["text"]

console.print(Panel(letra, title="🎶 Letra Transcrita", subtitle="Powered by Whisper + Rich", style="bold cyan"))
