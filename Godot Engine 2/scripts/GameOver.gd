extends Node2D

onready var select = get_node("SpinBox")
onready var ui_hisocre = get_node("C/VBoxC/HI")
onready var ui_score = get_node("C/VBoxC/SCORE")
onready var ui_contiune = get_node("C/VBoxC/Continue")
onready var ui_end = get_node("C/VBoxC/End")
onready var font_color = Color("555555")
onready var font_color_active = Color("FFFFFF")

func _ready():
	set_process_input(true)
	select.get_value()
	highlight_text()
	if Global.score > Global.high_score:
		Global.high_score = Global.score
	ui_score.text = "SCORE " + str(Global.score)
	ui_hisocre.text = "HI " + str(Global.high_score)

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
			get_tree().change_scene("res://scenes/Game.tscn")
			Global.Reset()
		elif selected == 2:
			get_tree().change_scene("res://scenes/MainMenu.tscn")

func highlight_text():
	if select.get_value() == 1:
		ui_contiune.set("custom_colors/font_color",font_color_active)
		ui_end.set("custom_colors/font_color",font_color)
	if select.get_value() == 2:
		ui_contiune.set("custom_colors/font_color",font_color)
		ui_end.set("custom_colors/font_color",font_color_active)
