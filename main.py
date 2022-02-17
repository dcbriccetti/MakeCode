radio.set_group(1)
delay_units = 0
unit_value = 250
tones = [
    Note.C3, Note.E3, Note.G3, Note.BB3,
    Note.C4, Note.E4, Note.G4, Note.BB4,
    Note.C5, Note.E5
]
basic.show_number(delay_units)

def on_button_pressed_a():
    global delay_units
    if delay_units > 0:
        delay_units -= 1
        music.ring_tone(tones[delay_units])
        basic.show_number(delay_units)
        music.stop_all_sounds()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global delay_units
    if delay_units < 9:
        delay_units += 1
        music.ring_tone(tones[delay_units])
        basic.show_number(delay_units)
        music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_string(receivedString):
    if receivedString == 'go':
        basic.pause(unit_value * delay_units)
        music.ring_tone(tones[delay_units])
        servos.P1.set_angle(90)
        basic.pause(500)
        servos.P1.set_angle(178)
        music.stop_all_sounds()
    elif receivedString == 'play':
        music.play_tone(tones[delay_units], 1000)
radio.on_received_string(on_received_string)
