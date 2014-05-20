while True:
    blockHits = mc.events.pollBlockHits()
        if blockHits:
            for blockHit in blockHits:
                print blockHit.pos.x
                print blockHit.pos.y
                print blockHit.pos.z
                print blockHit.face
                print blockHit.type
                print blockHit.entityID
