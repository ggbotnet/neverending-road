extends KinematicBody2D

const pos_limit = 33
const max_left = 81
const max_right = 147
var player_is_moving = false
var car = preload("res://graphics/player.png")
var cardmg = preload("res://graphics/player_dmg.png")
onready var root = get_node(".")
onready var sprite = get_node("Sprite")
onready var effect_hit = get_node("effect_hit")
onready var animation_player = get_node("AnimationPlayer")
onready var pickup_text = get_node("pickuptext")
onready var audio_pickup = get_node("Audio_PickUp")
onready var audio_crash = get_node("Audio_Crash")

func _ready():
	set_process_input(true)
	sprite.set_texture(car)
	effect_hit.hide()
	pickup_text.hide()
	for car in get_tree().get_nodes_in_group("Car"):
		car.connect("player_crash", self, "Game_Over")

func _input(event):
	if Global.gameover:
		return
	if event.type == InputEvent.KEY and event.pressed:
		if Input.is_action_pressed("keyboard_left") and root.get_pos().x > max_left:
			player_move(Vector2(-1, 0))
			player_is_moving = true
		if Input.is_action_pressed("keyboard_right") and root.get_pos().x <= max_right:
			player_move(Vector2(1, 0))
			player_is_moving = true

func player_move(dir):
	if not player_is_moving:
		var new_position = get_global_pos() + dir * pos_limit
		var time = 0.2
		var passed = 0.0
		while passed < time:
			var pt = passed / time
			var pos = get_global_pos().linear_interpolate(new_position, pt)
			set_global_pos(pos)
			passed += get_process_delta_time()
			yield(get_tree(), "idle_frame")
		set_global_pos(new_position)
		player_is_moving = false

func PickUp_Fuel():
	pick_text_show("FUEL")

func PickUp_Fruit():
	pick_text_show("10")

func pick_text_show(text):
	pickup_text.show()
	pickup_text.text = text
	audio_pickup.play()
	var timer = Timer.new()
	add_child(timer)
	timer.set_wait_time(0.3)
	timer.connect("timeout", self, "pick_text_hide")
	timer.set_one_shot(true)
	timer.start()

func pick_text_hide():
	pickup_text.hide()

func Game_Over():
	Global.gameover = true
	sprite.set_texture(cardmg)
	effect_hit.show()
	animation_player.play("hit")
	audio_crash.play()
	var timer = Timer.new()
	add_child(timer)
	timer.set_wait_time(0.4)
	timer.connect("timeout", self, "Game_Over_Scene")
	timer.set_one_shot(true)
	timer.start()

func Game_Over_Scene():
	get_tree().change_scene("res://scenes/GameOver.tscn")
