extends Node2D

var road_length = 300
var road_reset = -60
var egg = false
var egg_score = 0
var egg_number = randi() % 106 + 15
const cars = preload("res://scenes/Cars.tscn")
const fuel = preload("res://scenes/Fuel.tscn")
const trees = preload("res://scenes/Tree.tscn")
const fruits = preload("res://scenes/Fruits.tscn")
onready var roads = []
onready var timer_score = get_node("TimerScore")
onready var timer_fuel = get_node("TimerFuel")
onready var timer_fuel_spawn = get_node("TimerSFuel")
onready var timer_cars = get_node("TimerCars")
onready var timer_tree_left = get_node("TimerTreeLeft")
onready var timer_tree_right = get_node("TimerTreeRight")
onready var timer_fruits = get_node("TimerFruits")
onready var timer_egg = get_node("TimerEGG")
onready var ui_score = get_node("GUI/C/Score")
onready var ui_hiscore = get_node("GUI/C/HiScore")
onready var ui_fuel = get_node("GUI/C/FuelBar")

func _ready():
	set_process_input(true)
	set_fixed_process(true)
	timer_score.start()
	timer_fuel.start()
	timer_fuel_spawn.start()
	timer_cars.start()
	timer_tree_left.start()
	timer_tree_right.start()
	timer_fruits.start()
	ui_hiscore.text = str(Global.high_score)
	for nr in range(1,11):
		roads.append(get_node("Road" +str(nr)))
	egg_score = egg_number

func _input(event):
	if event.is_action_pressed("keyboard_esc"):
		get_tree().change_scene("res://scenes/MainMenu.tscn")
		Global.Reset()

func _fixed_process(delta):
	if Global.gameover == false:
		ui_score.text = str(Global.score)
		ui_fuel.set_value(Global.fuel)
		for road in roads:
			road.set_pos(Vector2(road.get_pos().x, road.get_pos().y + Global.speed_ground))
			if road.get_global_pos().y >= road_length:
				road.set_global_pos(Vector2(road.get_global_pos().x, road_reset))
	if Global.gameover == true:
		timer_score.stop()
	if Global.fuel < 1:
		Out_of_Fuel()
	if Global.score == egg_score:
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
	var timer = Timer.new()
	add_child(timer)
	timer.set_wait_time(0.4)
	timer.connect("timeout", self, "Game_Over_Scene")
	timer.set_one_shot(true)
	timer.start()

func Game_Over_Scene():
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
		tree_new.set_global_pos(Vector2(rand_range(0,44), tree_new.get_global_pos().y))
		add_child(tree_new)
		timer_tree_left.wait_time = rand_range(0.1,0.9)

func _on_TimerTreeRight_timeout():
	if not Global.gameover:
		var tree_new = trees.instance()
		tree_new.set_global_pos(Vector2(rand_range(214,254), tree_new.get_global_pos().y))
		add_child(tree_new)
		timer_tree_right.wait_time = rand_range(0.1,0.9)

func _on_TimerEGG_timeout():
	if not Global.gameover:
		if egg == false:
			egg = true
			var ufo = preload("res://scenes/UFO.tscn").instance()
			add_child(ufo)

func _on_TimerFruits_timeout():
	if not Global.gameover:
		var fruit_new = fruits.instance()
		add_child(fruit_new)
		timer_fruits.wait_time = rand_range(6,18)
