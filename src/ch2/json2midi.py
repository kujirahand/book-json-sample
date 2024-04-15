import json, mido

def main():
    # JSONファイルを読む --- (※1)
    with open('kaeru-uta.json', encoding='utf-8') as fp:
        data = json.load(fp)
    save_to_midi(data, 'kaeru-uta.mid')

def save_to_midi(data, midifile):
    # MIDIファイルを準備 --- (※2)
    midi = mido.MidiFile()
    track = mido.MidiTrack()
    # トラックにノート(発音)を追加 --- (※3)
    tm = 0
    for v in data:
        note = v['note']
        length = v['length']
        # 発音か休符か判定 --- (※4)
        if note >= 0:
            track.append(mido.Message('note_on', note=note, time=tm))
            track.append(mido.Message('note_off', note=note, time=length))
            tm = 0
        else:
            tm += length # 休符ならtmを増やす
            continue
    # MIDIファイルを保存 --- (※5)
    midi.tracks.append(track)
    midi.save(midifile)

if __name__ == '__main__': main()
