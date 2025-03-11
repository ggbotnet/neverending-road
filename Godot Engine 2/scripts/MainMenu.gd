extends Node2D

var scene_game = preload("res://scenes/Game.tscn")
onready var ui_newgame = get_node("Control/VBoxC/NewGame")
onready var ui_exit = get_node("Control/VBoxC/Exit")
onready var select = get_node("SpinBox")
onready var hiscore = get_node("Control/VBoxC/HiScore")
var font_color = Color("555555")
var font_color_active = Color("FFFFFF")

func _ready():
	set_process_input(true)
	select.get_value()
	highlight_text()
	if Global.score > Global.high_score:
		Global.high_score = Global.score
	hiscore.text = "HI-SCORE " +str(Global.high_score)

func _input(event):
	if Input.is_action_pressed("keyboard_esc"):
		get_tree().quit()
		return
	if Input.is_action_pressed("keyboard_down"):
		select.set_value(2)
		highlight_text()
	if Input.is_action_pressed("keyboard_up"):
		select.set_value(1)
		highlight_text()
	if Input.is_action_pressed("keyboard_enter"):
		var selected = select.get_value()
		if selected == 1:
			get_tree().change_scene_to(scene_game)
			Global.Reset()
		elif selected == 2:
			get_tree().quit()

func highlight_text():
	if select.get_value() == 1:
		ui_newgame.set("custom_colors/font_color",font_color_active)
		ui_exit.set("custom_colors/font_color",font_color)
	if select.get_value() == 2:
		ui_newgame.set("custom_colors/font_color",font_color)
		ui_exit.set("custom_colors/font_color",font_color_active)
