extends Node

var gameover = false
var speed_ground = 4
var fuel = 60
var score = 0
var high_score = 0: set = set_high_score
const filepath = "user://score.data"
@onready var music: AudioStreamPlayer = $Music
const mute_action: String = "keyboard_mute"
var is_mute: bool = false

func _ready():
	ProjectSettings.set_setting("application/run/main_loop/target_fps", 60)
	music.play()
	load_score()

func _input(_event: InputEvent) -> void:
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func toggle_mute() -> void:
	var bus_idx: int = AudioServer.get_bus_index("Master")
	is_mute = not is_mute
	AudioServer.set_bus_mute(bus_idx, is_mute)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed(mute_action) and event.pressed:
		toggle_mute()

func Reset():
	fuel = 60
	score = 0
	gameover = false

func set_high_score(new_value):
	high_score = new_value
	save_score()

func save_score():
	var file = FileAccess.open(filepath, FileAccess.WRITE)
	if file:
		file.store_var(high_score)
		file.close()

func load_score():
	var file = FileAccess.open(filepath, FileAccess.READ)
	if file:
		high_score = file.get_var()
		file.close()
