extends Node2D

onready var select = $SpinBox
onready var ui_hisocre = $C/VBoxC/HI
onready var ui_score = $C/VBoxC/SCORE
onready var ui_contiune = $C/VBoxC/Continue
onready var ui_end = $C/VBoxC/End

func _ready():
	if Global.score > Global.high_score:
		Global.high_score = Global.score
	ui_score.text = "SCORE " + str(Global.score)
	ui_hisocre.text = "HI " + str(Global.high_score)

func _physics_process(_delta):
	var textcolor = Color("555555")
	var textcolorsel = Color("FFFFFF")
	if select.value == 1:
		ui_contiune.set("custom_colors/font_color",textcolorsel)
		ui_end.set("custom_colors/font_color",textcolor)
		if Input.is_action_just_pressed("keyboard_enter"):
			# warning-ignore:return_value_discarded
			get_tree().change_scene("res://scenes/Game.tscn")
			Global.Reset()
	if select.value == 2:
		ui_contiune.set("custom_colors/font_color",textcolor)
		ui_end.set("custom_colors/font_color",textcolorsel)
		if Input.is_action_just_pressed("keyboard_enter"):
			# warning-ignore:return_value_discarded
			get_tree().change_scene("res://scenes/MainMenu.tscn")

func _input(event):
	if event.is_action_pressed("keyboard_esc"):
		get_tree().quit()
	if event.is_action_pressed("keyboard_down"):
		select.value = 2
	if event.is_action_pressed("keyboard_up"):
		select.value = 1
