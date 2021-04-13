msg = "Hello World!"
mySprite = sprites.create(assets.image("""
    smiley
"""), SpriteKind.player)
scene.set_background_color(10)
mySprite.say(msg)
print("Hello console")