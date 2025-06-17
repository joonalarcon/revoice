# Entrenamiento de Voz con so-vits-svc y Spleeter

Este proyecto permite entrenar un modelo de voz personalizado usando so-vits-svc para conversión de voz cantada.  
Puedes separar la voz y la música con Spleeter antes del entrenamiento.

## Características

- Separación de voz con [Spleeter](https://github.com/deezer/spleeter)
- Entrenamiento de conversión de voz con [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)
- Genera voz cantada usando tu modelo entrenado

## Requisitos

- Python 3.8 o superior
- PyTorch
- TensorFlow
- ffmpeg
- Otras dependencias listadas en `requirements.txt`

## Instalación

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
pip install -r requirements.txt
