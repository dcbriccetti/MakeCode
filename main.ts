radio.setGroup(1)
let delay_units = 0
let unit_value = 250
let tones = [Note.C3, Note.E3, Note.G3, Note.Bb3, Note.C4, Note.E4, Note.G4, Note.Bb4, Note.C5, Note.E5]
basic.showNumber(delay_units)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (delay_units > 0) {
        delay_units -= 1
        music.ringTone(tones[delay_units])
        basic.showNumber(delay_units)
        music.stopAllSounds()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (delay_units < 9) {
        delay_units += 1
        music.ringTone(tones[delay_units])
        basic.showNumber(delay_units)
        music.stopAllSounds()
    }
    
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    if (receivedString == "go") {
        basic.pause(unit_value * delay_units)
        music.ringTone(tones[delay_units])
        servos.P1.setAngle(90)
        basic.pause(500)
        servos.P1.setAngle(178)
        music.stopAllSounds()
    } else if (receivedString == "play") {
        music.playTone(tones[delay_units], 1000)
    }
    
})
