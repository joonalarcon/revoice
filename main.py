from spleeter.separator import Separator

import_audio = './rod.mp3'
output_audio = 'vocals/'

separator = Separator('spleeter:2stems')
separator.separate_to_file(import_audio, output_audio)

print('Separacion de audio completada')