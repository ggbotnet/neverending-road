extends Node2D

var scene_game = preload("res://scenes/Game.tscn")
onready var ui_newgame = $Control/VBoxC/NewGame
onready var ui_exit = $Control/VBoxC/Exit
onready var select = $SpinBox
onready var hiscore = $Control/VBoxC/HiScore

func _ready():
	if Global.score > Global.high_score:
		Global.high_score = Global.score
	hiscore.text = "HI-SCORE " +str(Global.high_score)

func _physics_process(_delta):
	var textcolor = Color("555555")
	var textcolorsel = Color("FFFFFF")
	if select.value == 1:
		ui_newgame.set("custom_colors/font_color",textcolorsel)
		ui_exit.set("custom_colors/font_color",textcolor)
		if Input.is_action_just_pressed("keyboard_enter"):
			# warning-ignore:return_value_discarded
			get_tree().change_scene_to(scene_game)
			Global.Reset()
	if select.value == 2:
		ui_newgame.set("custom_colors/font_color",textcolor)
		ui_exit.set("custom_colors/font_color",textcolorsel)
		if Input.is_action_just_pressed("keyboard_enter"):
			get_tree().quit()

func _input(event):
	if event.is_action_pressed("keyboard_esc"):
		get_tree().quit()
	if event.is_action_pressed("keyboard_down"):
		select.value = 2
	if event.is_action_pressed("keyboard_up"):
		select.value = 1
