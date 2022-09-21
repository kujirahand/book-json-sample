import mido
for msg in mido.MidiFile('kaeru-uta.mid'):
    print(msg)

