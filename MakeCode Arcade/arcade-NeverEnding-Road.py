@namespace
class SpriteKind:
    Fuel = SpriteKind.create()
    Fruit = SpriteKind.create()
def Game():
    global carPlayer
    carPlayer = sprites.create(img("""
            ...eeeeeeeee....
                    ..e2e22222e2e...
                    .eeee22222eeee..
                    .e22222222222ef.
                    .e22eeeeeee22ef.
                    .e2e9999999e2ef.
                    eee999999999eee.
                    .e9e9999999e9eff
                    .e99e99999e99ef.
                    .e99eeeeeee99ef.
                    .e99e22222e99ef.
                    .eeee22222eeeef.
                    .e99e22222e99ef.
                    .eeeeeeeeeeeeef.
                    .e22222222222ef.
                    .e22e22222e22ef.
                    .e22e22222e22ef.
                    .e22eeeeeee22ef.
                    .e22eeeeeee22ef.
                    .e22222222222ef.
                    ..eeeeeeeeeeeff.
                    ...fffffffffff..
        """),
        SpriteKind.player)
    carPlayer.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    carPlayer.set_position(96, 104)
    carPlayer.z = 3
    info.set_life(2)
    info.set_score(0)
    info.start_countdown(8)
    scene.set_background_image(img("""
        777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
                777777777777ddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd777777777777
    """))
    scene.set_background_color(11)
def MainMenu():
    global Title
    Title = sprites.create(img("""
            8ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff8888888
                    8ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff8888888
                    88ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff888888
                    88ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff888888
                    88ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff888888
                    888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888
                    888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888
                    888ffffffff8ffffffffffffffffffffff8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffff888888fffffffffffffffff8ffffffff8fffffffffffffff88888
                    fff88888888ff111ff11ff1111111ff11fff11ff1111111ff111111fff1111111ff111ff11ff111111fff11ff111ff11fff111111f8fffffff111111ffff11111ffff11111fff111111ff888888fffff
                    ffff88888888f111ff11ff1111111ff11fff11ff1111111ff1111111ff1111111ff111ff11ff1111111ff11ff111ff11ff1111111fffffffff1111111ff1111111ff1111111ff1111111ff888888ffff
                    ffff88888888f111ff11ff11fffffff11fff11ff11fffffff11fff11ff11fffffff111ff11ff11fff11ff11ff111ff11ff11ffffffffffffff11fff11ff11fff11ff11fff11ff11fff11fff88888ffff
                    ffff88888888f1111f11ff11fffffff11fff11ff11fffffff11fff11ff11fffffff1111f11ff11fff11ff11ff1111f11ff11ffffffffffffff11fff11ff11fff11ff11fff11ff11fff11fff88888ffff
                    fffff8888888f1111f11ff111111fff11fff11ff111111fff1111111ff111111fff1111f11ff11fff11ff11ff1111f11ff11ff111fff8fffff1111111ff11fff11ff11fff11ff11fff11fff888888fff
                    fffff8888888f1111111ff111111ffff11f111ff111111fff111111fff111111fff1111111ff11fff11ff11ff1111111ff11ff111fff8fffff111111fff11fff11ff11fff11ff11fff11fff888888fff
                    fffff8888888f11f1111ff11ffffffff11f11fff11fffffff11ff11fff11fffffff11f1111ff11fff11ff11ff11f1111ff11fff11fff8fffff11ff11fff11fff11ff11fff11ff11fff11fff888888fff
                    fffff8888888f11f1111ff11ffffffff11f11fff11fffffff11ff11fff11fffffff11f1111ff11fff11ff11ff11f1111ff11fff11fff8fffff11ff11fff11fff11ff1111111ff11fff11fff888888fff
                    888888fffffff11ff111ff11fffffffff1111fff11fffffff11ff11fff11fffffff11ff111ff11fff11ff11ff11ff111ff11fff11fffff888f11ff11fff11fff11ff1111111ff11fff11ffffffffff88
                    888888fffffff11ff111ff1111111f88f111ffff1111111ff11ff111ff1111111ff11ff111ff1111111ff11ff11ff111ff1111111fffff888f11ff111ff1111111ff11fff11ff1111111ffffffffff88
                    888888fffffff11ff111ff1111111ffff111ffff1111111ff11fff11ff1111111ff11ff111ff111111fff11ff11ff111fff111111fffff888f11fff11fff11111fff11fff11ff111111fffffffffff88
                    8888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88ffffffffffffffffffffffffffffffffffffffffffffff8
                    8888888fffffffffffffffffffffffff88fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888ffffffffffffffffffffffffffffffffffffffffffff8
                    8888888fffffffffffffffffffffffff88ffffffffffffffffffff8ffffffffffffffffffffffffffffff8fffffffffffff8fffffffffff8888fffffffffffffffff8fffffffffffffffff8ffffffff8
                    8888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff8
                    88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff
                    ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888
                    8ffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff8888888
                    8ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff8888888
                    8ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff8888888
                    8fffffffff8888888fffffffff8888888fffffffff88888888fffffff22222222222222222222222222222222288888888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff888888
                    8fffffffff88ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb888fffff222ffffffffffffffffff222fffffffffffffff8888fffffffff8888888fffffffff8888888fffffffff8888888fffffffff888888
                    88ffffffff88888888ffffffff88888888ffffffff88888888ff222ff99991f111111111191ff22f9119199111111ff888ffffffff88888888ffffffff88888888ffffffff88888888ffffffff888888
                    88ffffffff88888888ffffffff88888888ffffffff888888822222f9999119f11111111191919f22f99919999911111ff8ffffffff88888888ffffffff88888888ffffffff88888888ffffffff888888
                    fff888888ccbbbbbbbbbbbbbbbbbbbbbbbbbbb88888fff22222222f9911191f111111119191999f22f999919199911111ff8888888fffffffff8888888fffffffff8888888fffffffff8888888ffffff
                    fff88f8f8f8ffffffff88f8f8c8ffffffff88f888822222222222f99119911f1111111919199999ff2f9999991199991111fff8f888ffffffff88f8f8f8ffffffff88f8f8f8ffffffff88f8f8f8fffff
                    fff88888888ffffffff88888888ffffffff888ce2222222222222f11991111f111111919199999222f2ff9999999119999111ff8822ffffffff88888888ffffffff88888888ffffffff88888888fffff
                    fff88fccbbbbbbbbbbbbbbbbbbbbfffffff8c222eeeeee222222f199911111f1111991919999922222f22f99999999111199911f2222fffffff88f8f8f8ffffffff88f8f8f8ffffffff88f8f8f8fffff
                    ffff8888888cffffffff88888888ffff22222222222222eeeeeeeffffffffff111991919999992222fff22f99999999999999999f222ffffffff8888888fffffffff8888888fffffffff8888888fffff
                    ffff8f8f8f8fffffffff8f8f888cffeeeeeee222222222222222222222222effffffffffffffffffffffff2ffffffffffffffffffeee22efffff88888f88ffffffff888f8f8fffffffff888f8f8fffff
                    fffccbbbbbbbbbbbbbbb888ceeeeee2222222eeeeeeeee22222222222222e2222222222222222222222222e22222222222eeee2222effffeeeeeeeeeeeeeefffffff88888888ffffffff88888888ffff
                    fffff8c888c8fffffffff88e2222222222222222222222eeeeee2222222e22222222222222222222222222e222222222222222eeee2222eeee22222222222eeeeffff8888888fffffffff8888888ffff
                    8888fffffffff88f8f88ffff2222222222fffff2222222222222eeeeeeee22222222222222222222222222e222222ffffff2222222eee22222eee2222222222222ee8ffffffff8888888fffffffff888
                    ccbbbbbbbbbbbbbbbbbb8fff22222222ffffffff2222222222222222222eeeeeeeee22222222222222222e22222fffffffff222222222eeee222eeee222222222222eefffffff8f8f8f88ffffffff8f8
                    8f8f8fffffffff8f8f8f8fff2222222fffccccccf222222222222222222e22222222eeeeeeee222222222e2222fffcccccccf222222222222ee22222ee22222222222eeeefffff8f8f8f8fffffffff8f
                    ffff8fffffffffffffff8fff222222ffcccccccccf2222222222eeeeeeeeee22222222222222eeeeeee22eee2ffcccbbcccccf2222222222222eeeeeeeee22222252222e22efff8fffff8fffffffff8f
                    8f8ccbbbbbbbbbbbbbb888f2244422ffcccbbbccccf22222222eeeeeeeeeeeeeeeeeeeeeeeeee222222ee222ffccbbbbbbccccf22222222222222ee22222e22222222222ee2eff888f8f88ffffffff8f
                    fff8f8ffffffff88ccc8f8f224442ffccbbbfcbbccf22222222effffffffffff22222222222222222222e222fccbbffbbcbcccffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee2ef8ffffff8ffffffff8f
                    f88888fffffffff8fff888f222222ffccbbbcffbcccf2222222eeeeeeeeeeeeeeeeeeeeeeeeeee222222e22ffccbffbbbffbcccf224444222222222ee22222e222222222222eeff8888888fffffffff8
                    888888ccbbbbbbbbbbbc88f22222fffcbffbbbbbbccf2222222efffffffffff222222222222222222222e22fccbbbbbbbbffbccfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeff8888888fffffffff8
                    fffffffeeeeeeeefffffffff2222ffccbfcbbbbbbccf2222222eeeeeeeeeeeeeeeeeeeeeeeeeee222222e22fccbbbbbbbbbcbccf2222222222222222e44444fffffffffffff44ffffffffffeeeeeeeef
                    ffffffeeffffffffffffffef2222ffccbcbbbbbffbcf22eeee22efffffffff2222222222222222222222e22fccbcbbbcbbbbbccf2222222222222222ebbbbbfcccccccccccfbbfffffffffeeeeeeeeff
                    fffffffefccbbbbbbbbbbcfff222ffccbbbbfbbcfbcf22eeee22eeeeeeeeeeeeeeeeeeeeeeeee2222222e2ffccbfcbcfbbbbbccfeeeeeeeeeeeeeeeeeeeeeefffffffffffffeeffffffffffefefeffff
                    fffffeeeeeeeeffffffffeeeff22ffccbbbbbbbbbccff22222222222222e222222222222222222222222e2ffccbfcbbbbbcfbccf2222222222222222222222222222222222222ffffffffeeeeeeeefff
                    fefeffffffffffffffffffffffffffccbfcbbbbbbccff22222222222222e222222222222222222222222e2ffccbcbbbbbbffbccfcccccccccccccccccccccccccccccccccccccefefefefffffffffefe
                    eeefffffffffccbbbbbbbbbbbfffffccbcfbbbfbbccff22222222222222e222222222222222222222222e2fffccbbbbbbbfbbccfccccccccccccccccccccccccccccccccccccceeeeeefffffffffeeee
                    fefffffffffefcfefefffffffffefefccbcbbffbcccffcccccccccccccccccccccccccccccccccccccccccfffccbbcffbbbbccfcfffffffffffffffffffffffffffffffffffffefefefffffffffefeff
                    efffffffffefefefefffffffffefefefccbbbcbbcccfcfffffffffffffffffffffffffffffffffffffffffffffccbbcfcbbcccfccfefefeccccccccccccccccfefffffffffefefefefffffffffefefef
                    fffefefefefffffffffefefefefffffffcccbbccccfccffffffeffffffffcccccccccffefffffffffffefffefffcccbbbccccfccfefffffffcccccccccccccfffffefefefefffffffffefefefeffffff
                    ffefefefefffffffffefefefeffffffffccccccccfccffffffffffffffffcccccccccfffffffffffffffffffffffccccccccfccfffffffffffccccccccccffffffefefefefffffffffefefefefffffff
                    fefefefefffffffffefefefefffffffffffcccccfccfffffffffffffffffffcccccfffffffffffffffffffffffffffcccccfcfffffffffffffffcccccccffffffffffffefffffffffefefefeffffffff
                    efffefefffffffffefefefeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffefeeeefffffffffefefefefffffffff
                    fffffffefefefefffffffffefefefefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffefefffffffffefefefefffffffffefefefeff
                    ffffffffffffffefffffffffffefffeffffffffefeeffeeffffffffefffffffffffffffeffffffeffffffffffffffffffffffffefffffffffffffffeeeefefeffffffffeefefefefffffffffefffffef
                    ffffffefffffeeffffffffefffffeeffffffffefffffeeffffffffeeeeefeeffffffffeeeeeeeeffffffffefffffffffffffffeeeeefeeffffffffefffffeeffffffffefffffeeffffffffefffffeeff
                    fffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeeffffffffeeeeeeeefff
                    eefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffefefefeeffffffffeff
                    efefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffefefefffffffffffef
                    efefffffffffeeeeeeefffffffffeeeeeeefffffffffeffeeeefffffffffeffefeefffffffffeeeeeeefffffffffefeeeeefffffffffeeeeeeefffffffffeeeeeeefffffffffeeeeeeefffffffffeeef
                    efefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefefefefffffffffefef
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1122222222211fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff112222222222211ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    fffffffffffffffff111111ff111111ff1111111ff11111fff11111ffffffffff122222111222221fffffffff111111ff11111ffffffffff111111ff11ffffffff111ffff11ff11fffffffffffffffff
                    fffffffffffffffff11fff11f11fff11f11ffffff11fff11f11fff11fffffffff122221121122221fffffffffff11fff11fff11fffffffff11fff11f11fffffff11f11fff11ff11fffffffffffffffff
                    fffffffffffffffff11fff11f11fff11f11ffffff11ffffff11ffffffffffffff122211222112221fffffffffff11fff11fff11fffffffff11fff11f11ffffff11fff11ff11ff11fffffffffffffffff
                    fffffffffffffffff111111ff111111ff11111ffff11111fff11111ffffffffff122211222112221fffffffffff11fff11fff11fffffffff111111ff11ffffff11fff11fff1111ffffffffffffffffff
                    fffffffffffffffff11ffffff11f11fff11fffffffffff11ffffff11fffffffff122211111112221fffffffffff11fff11fff11fffffffff11ffffff11ffffff1111111ffff11fffffffffffffffffff
                    fffffffffffffffff11ffffff11ff11ff11ffffff11fff11f11fff11fffffffff122211222112221fffffffffff11fff11fff11fffffffff11ffffff11ffffff11fff11ffff11fffffffffffffffffff
                    fffffffffffffffff11ffffff11fff11f1111111ff11111fff11111ffffffffff122211222112221fffffffffff11ffff11111ffffffffff11ffffff1111111f11fff11ffff11fffffffffffffffffff
                    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff112222222222211ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1122222222211fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffcfffffffccfffcffcfffcfcccfffffccffcfcffffffccfffccffccfffcffcccfcffcfcccfcccfffffffcccfcccfcccfcccffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffcfcfffffcffffcfcfccfccfcfffffffcfcfcfcfffffcffffcffffcfcfcfcffcffccfcfcffffcffffffffffcfcfcfffcfcffffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffcccfffffcfccfcccfcfcfcfccffffffccfffcffffffcfccfcfccfccffcfcffcffcfccfccfffcffffffffcccfcfcfcccfcccffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffcfcfffffcffcfcfcfcfffcfcfffffffcfcffcffffffcffcfcffcfcfcfcfcffcffcffcfcffffcffffffffcfffcfcfcfffffcffffffffffffffffffffffffffffff
                    fffffffffffffffffffffffffffffffcfcffffffcccfcfcfcfffcfcccfffffccfffcfffffffcccffcccfccfffcfffcffcffcfcccffcffcfffffcccfcccfcccfcccffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """),
        SpriteKind.player)
    game.set_dialog_frame(img("""
        . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . .
    """))
    game.set_dialog_cursor(img("""
        . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . .
    """))
    game.show_long_text("", DialogLayout.BOTTOM)
    Title.z = 99
    sprites.destroy(Title, effects.disintegrate, 500)
    music.play(music.melody_playable(music.jump_up),
        music.PlaybackMode.IN_BACKGROUND)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    info.change_score_by(5)
    carPlayer.start_effect(effects.confetti, 300)
    music.play(music.melody_playable(music.magic_wand),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Fruit, on_on_overlap)

def on_left_pressed():
    if carPlayer.x > 30:
        carPlayer.x += -33
        pause(100)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_countdown_end():
    GameOver()
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    if carPlayer.x < 129:
        carPlayer.x += 33
        pause(100)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2)
    info.change_countdown_by(randint(2, 10))
    carPlayer.start_effect(effects.spray, 300)
    music.play(music.melody_playable(music.beam_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Fuel, on_on_overlap2)

def on_life_zero():
    GameOver()
info.on_life_zero(on_life_zero)

def GameOver():
    game.set_game_over_message(True, "GAME OVER!")
    game.set_game_over_effect(True, effects.dissolve)
    game.set_game_over_playable(True, music.melody_playable(music.power_down), False)
    game.game_over(True)

def on_on_overlap3(sprite3, otherSprite3):
    otherSprite3.destroy()
    carPlayer.start_effect(effects.fire, 200)
    scene.camera_shake(4, 200)
    music.play(music.melody_playable(music.small_crash),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_life_by(-1)
    pause(100)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

posRight: List[number] = []
posLeft: List[number] = []
pos_all: List[number] = []
Fruits: List[Image] = []
Spawn_Fruit: Sprite = None
Spawn_Fuel: Sprite = None
roadLine3: Sprite = None
roadLine2: Sprite = None
roadLine1: Sprite = None
carEnemy02: Sprite = None
carEnemy01: Sprite = None
Title: Sprite = None
carPlayer: Sprite = None
MainMenu()
Game()
scene.set_background_color(11)

def on_on_update():
    if carEnemy01:
        if carEnemy01.y > scene.screen_height():
            sprites.destroy(carEnemy01)
    if carEnemy02:
        if carEnemy02.y > scene.screen_height():
            sprites.destroy(carEnemy02)
    if roadLine1:
        if roadLine1.y > scene.screen_height():
            sprites.destroy(roadLine1)
            sprites.destroy(roadLine2)
            sprites.destroy(roadLine3)
    if Spawn_Fuel:
        if Spawn_Fuel.y > scene.screen_height():
            sprites.destroy(Spawn_Fuel)
    if Spawn_Fruit:
        if Spawn_Fruit.y > scene.screen_height():
            sprites.destroy(Spawn_Fruit)
game.on_update(on_on_update)

def on_update_interval():
    global Spawn_Fruit, Fruits, pos_all
    Spawn_Fruit = sprites.create(img("""
        .
    """), SpriteKind.Fruit)
    Fruits = [img("""
            . . . d d d d d d d . . . . . . 
                    . . d d 1 1 1 d d 1 d d . . . . 
                    . e d d 1 1 1 1 1 1 1 d d . . . 
                    . e e d d 1 1 1 1 1 1 1 d d . . 
                    e e e e d d d 1 1 1 1 1 d d . . 
                    e e e e e d d d 1 1 1 1 1 d d . 
                    e e e e e e d d d 1 1 1 1 1 d f 
                    e e e e e e e e d d d 1 1 1 d f 
                    e e e e e e e e e e d d d d d f 
                    . e e e e e e e e e e e d d f f 
                    . e e e e e e e e e e e e e f . 
                    . . e e e e e e e e e e e e f . 
                    . . e e e e e e e e e e e f f . 
                    . . . e e e e e e e e e f f . . 
                    . . . . e e e e e e f f f . . . 
                    . . . . . . f f f f f . . . . .
        """),
        img("""
            . . . . . . . . f f f . . . . . 
                    . . . . . . . . . f 5 e . . . . 
                    . . . . . . . . . . e 5 e . . . 
                    . . . . . . . . . . . 1 5 e . . 
                    . . . . . . . . . . . 5 5 5 e . 
                    . . . . . . . . . . . 1 5 5 e f 
                    . . . . . . . . . . . 1 5 5 e f 
                    . . . . . . . . . . 1 5 5 5 e f 
                    . . . . . . . . . 1 5 5 5 5 e f 
                    . . . . . . . 1 1 5 5 5 e 5 e f 
                    . . e 5 5 5 5 5 5 5 5 e 5 5 f f 
                    f e 5 5 5 5 5 5 e e e 5 5 f f . 
                    f 5 5 5 5 e e e 5 5 5 5 f f . . 
                    . e e 5 5 5 5 5 5 e e f f . . . 
                    . . . e e e e e f f f f . . . . 
                    . . . . f f f f f . . . . . . .
        """),
        img("""
            . . . . . . 7 7 7 . . . . . . . 
                    . . . e e 6 6 6 7 7 . . . . . . 
                    . . e 4 e 6 6 6 6 7 7 . . . . . 
                    . 4 e e e f 6 6 6 6 7 7 . . . . 
                    . e e e 4 e f f 6 6 6 7 7 . . . 
                    e 4 e e e 4 4 5 f f 6 6 7 . . . 
                    e 4 e 4 e 4 5 5 5 4 f f . . . . 
                    e e 4 e 4 5 4 4 5 5 4 4 . . . . 
                    . 4 4 4 4 4 5 5 5 5 4 4 . . . . 
                    . e 5 e 5 4 5 5 5 5 4 5 4 . . . 
                    . . 4 5 4 5 5 5 5 5 5 4 5 4 . . 
                    . . 4 4 5 4 5 5 5 4 5 5 5 5 4 . 
                    . . . e 5 4 5 4 5 5 5 5 4 5 5 f 
                    . . . . e 4 5 5 5 5 4 5 4 5 f f 
                    . . . . . . 4 e 4 4 4 4 4 f f . 
                    . . . . . . . f f f f f f f . .
        """),
        img("""
            . . . . 5 4 e e e e . . . . . . 
                    . . . 5 7 7 5 4 e e e e . . . . 
                    . . 5 7 7 7 7 5 4 e e e e . . . 
                    . 5 7 f 7 f 7 7 5 e e e e e . . 
                    . 7 5 7 7 5 f 7 7 4 e e e e e . 
                    5 7 f 7 5 7 5 f 7 5 e e e e e f 
                    7 5 f 5 5 5 7 7 7 5 e e e e e f 
                    7 5 7 5 5 5 7 5 7 5 e e e e e f 
                    7 7 f 5 5 5 f 7 7 5 e e e e e f 
                    5 7 5 f 5 7 7 7 7 5 e e e e e f 
                    . 7 7 7 7 5 f 7 7 4 e e e e e f 
                    . 5 7 f 7 f 7 7 5 e e e e e f f 
                    . . 5 7 7 7 7 5 4 e e e e f f . 
                    . . . 5 7 7 5 4 e e e e f f . . 
                    . . . . 5 4 e e e e f f f . . . 
                    . . . . . . f f f f f . . . . .
        """)]
    Spawn_Fruit.set_image(Fruits._pick_random())
    Spawn_Fruit.set_velocity(0, 100)
    pos_all = [30, 63, 96, 129]
    Spawn_Fruit.set_position(pos_all._pick_random(), 0)
    Spawn_Fruit.z = 1
game.on_update_interval(randint(1100, 3900), on_update_interval)

def on_update_interval2():
    global Spawn_Fuel, pos_all
    Spawn_Fuel = sprites.create_projectile_from_side(img("""
            . . f f . . . . . . . . . . . . 
                    . f . f f f f f e e e e e e e . 
                    f . . . f f f 2 2 2 2 2 2 2 e f 
                    . . . . f f 2 2 2 2 f f f 2 e f 
                    . . . . f 2 2 2 2 2 2 . . 2 e f 
                    . . . . e 2 2 2 2 2 2 2 . 2 e f 
                    . . . . e 2 2 2 2 2 2 2 2 2 e f 
                    . . . . e 2 2 e 2 2 2 e 2 2 e f 
                    . . . . e 2 2 2 e e e 2 2 2 e f 
                    . . . . e 2 2 2 e 2 e 2 2 2 e f 
                    . . . . e 2 2 2 e e e 2 2 2 e f 
                    . . . . e 2 2 e 2 2 2 e 2 2 e f 
                    . . . . e 2 2 2 2 2 2 2 2 2 e f 
                    . . . . . e 2 2 2 2 2 2 2 e f f 
                    . . . . . . e e e e e e e f f . 
                    . . . . . . . f f f f f f f . .
        """),
        0,
        100)
    Spawn_Fuel.set_kind(SpriteKind.Fuel)
    pos_all = [30, 63, 96, 129]
    Spawn_Fuel.set_position(pos_all._pick_random(), 0)
    Spawn_Fuel.z = 1
game.on_update_interval(randint(2000, 6000), on_update_interval2)

def on_update_interval3():
    global carEnemy02, posLeft
    info.change_score_by(1)
    carEnemy02 = sprites.create_projectile_from_side(img("""
            ...888888888....
                    ..89866666898...
                    .8986666666898..
                    .8866666666688f.
                    .8668888888668f.
                    .8689999999868f.
                    .8899999999988f.
                    .8899999999988f.
                    889888888888988.
                    .8986666666898ff
                    .8986666666898f.
                    .8886666666888f.
                    .8986666666898f.
                    .8986666666898f.
                    .8988888888898f.
                    .8899999999988f.
                    .8688888888868f.
                    .8666666666668f.
                    .8886666666888f.
                    .8338666668338f.
                    .8888888888888f.
                    ..fffffffffffff.
        """),
        0,
        66)
    carEnemy02.set_kind(SpriteKind.enemy)
    posLeft = [30, 63]
    carEnemy02.set_position(posLeft._pick_random(), 0)
    carEnemy02.z = 2
game.on_update_interval(1000, on_update_interval3)

def on_update_interval4():
    global carEnemy01, posRight
    carEnemy01 = sprites.create_projectile_from_side(img("""
            ...888888888....
                    ..89866666898...
                    .8986666666898..
                    .8866666666688f.
                    .8668888888668f.
                    .8689999999868f.
                    .8899999999988f.
                    .8899999999988f.
                    889888888888988.
                    .8986666666898ff
                    .8986666666898f.
                    .8886666666888f.
                    .8986666666898f.
                    .8986666666898f.
                    .8988888888898f.
                    .8899999999988f.
                    .8688888888868f.
                    .8666666666668f.
                    .8886666666888f.
                    .8338666668338f.
                    .8888888888888f.
                    ..fffffffffffff.
        """),
        0,
        66)
    carEnemy01.set_kind(SpriteKind.enemy)
    posRight = [96, 129]
    carEnemy01.set_position(posRight._pick_random(), 0)
    carEnemy01.z = 2
game.on_update_interval(1800, on_update_interval4)

def on_update_interval5():
    global roadLine1, roadLine2, roadLine3
    roadLine1 = sprites.create_projectile_from_side(img("""
            d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d
        """),
        0,
        100)
    roadLine1.x = 46
    roadLine1.set_flag(SpriteFlag.GHOST, True)
    roadLine2 = sprites.create_projectile_from_side(img("""
            d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d
        """),
        0,
        100)
    roadLine2.x = 80
    roadLine2.set_flag(SpriteFlag.GHOST, True)
    roadLine3 = sprites.create_projectile_from_side(img("""
            d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d 
                    d d
        """),
        0,
        100)
    roadLine3.x = 112
    roadLine3.set_flag(SpriteFlag.GHOST, True)
game.on_update_interval(500, on_update_interval5)
