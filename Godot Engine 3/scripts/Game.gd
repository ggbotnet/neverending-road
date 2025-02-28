extends Node2D

var road_length := 300
var road_speed := -60
var egg = false
var egg_score = RandomNumberGenerator.new()
var egg_score_random = []
const cars = preload("res://scenes/Cars.tscn")
const fuel = preload("res://scenes/Fuel.tscn")
const trees = preload("res://scenes/Tree.tscn")
const fruits = preload("res://scenes/Fruits.tscn")
onready var roads = [$Road1, $Road2, $Road3, $Road4, $Road5, $Road6, $Road7, $Road8, $Road9, $Road10]
onready var timer_score = $TimerScore
onready var timer_fuel = $TimerFuel
onready var timer_fuel_spawn = $TimerSFuel
onready var timer_cars = $TimerCars
onready var timer_tree_left = $TimerTreeLeft
onready var timer_tree_right = $TimerTreeRight
onready var timer_fruits = $TimerFruits
onready var timer_egg = $TimerEGG
onready var ui_score = $GUI/C/Score
onready var ui_hiscore = $GUI/C/HiScore
onready var ui_fuel = $GUI/C/FuelBar

func _ready():
	timer_score.start()
	timer_fuel.start()
	timer_fuel_spawn.start()
	timer_cars.start()
	timer_tree_left.start()
	timer_tree_right.start()
	timer_fruits.start()
	ui_hiscore.text = str(Global.high_score)
	egg_score.randomize()
	var egg_score_new = egg_score.randi_range(15, 120)
	egg_score_random = egg_score_new

func _input(event):
	if event.is_action_pressed("keyboard_esc"):
		# warning-ignore:return_value_discarded
		get_tree().change_scene("res://scenes/MainMenu.tscn")
		Global.Reset()

func _physics_process(_delta: float) -> void:
	if Global.gameover == false:
		ui_score.text = str(Global.score)
		ui_fuel.value = Global.fuel
		for road in roads:
			road.transform.origin.y += Global.speed_ground
			if road.transform.origin.y >= road_length:
				road.transform.origin.y = road_speed
	if Global.gameover == true:
		timer_score.stop()
	if Global.fuel < 1:
		Out_of_Fuel()
	if Global.score == egg_score_random and timer_egg.is_stopped():
		timer_egg.start()

func Out_of_Fuel():
	Global.gameover = true
	timer_score.stop()
	timer_fuel.stop()
	timer_fuel_spawn.stop()
	timer_cars.stop()
	timer_tree_left.stop()
	timer_tree_right.stop()
	timer_fruits.stop()
	yield(get_tree().create_timer(0.2), "timeout")
	# warning-ignore:return_value_discarded
	get_tree().change_scene("res://scenes/GameOver.tscn")

func _on_TimerScore_timeout():
	Global.score += 1

func _on_TimerFuel_timeout():
	Global.fuel -= 1

func _on_TimerSFuel_timeout():
	if not Global.gameover:
		var fuel_new = fuel.instance()
		add_child(fuel_new)
		timer_fuel_spawn.wait_time = rand_range(3,15)

func _on_TimerCars_timeout():
	if not Global.gameover:
		var car_new = cars.instance()
		add_child(car_new)
		timer_cars.wait_time = rand_range(0.2,0.5)

func _on_TimerTreeLeft_timeout():
	if not Global.gameover:
		var tree_new = trees.instance()
		tree_new.transform.origin.x = rand_range(0,44)
		add_child(tree_new)
		timer_tree_left.wait_time = rand_range(0.1,0.9)

func _on_TimerTreeRight_timeout():
	if not Global.gameover:
		var tree_new = trees.instance()
		tree_new.transform.origin.x = rand_range(214,254)
		add_child(tree_new)
		timer_tree_right.wait_time = rand_range(0.1,0.9)

func _on_TimerEGG_timeout():
	if not Global.gameover:
		if timer_egg.is_stopped() and egg == false:
			egg = true
			var ufo = preload("res://scenes/UFO.tscn").instance()
			add_child(ufo)

func _on_TimerFruits_timeout():
	if not Global.gameover:
		var fruit_new = fruits.instance()
		add_child(fruit_new)
		timer_fruits.wait_time = rand_range(6,18)
