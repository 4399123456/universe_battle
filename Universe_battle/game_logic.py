import sys,time,random,os
import pygame
from Background import Background
from Health import Health
from settings import Settings
from Game_Info import Game_Info
from datetime import datetime
from Hero_Ship import Hero_Ship
from Bullet import Bullet
from Ship import Ship
from Enemy_Hero_Ship import Enemy_Hero_Ship
from Universe_Stuff import Universe_Stuff
from Explosion import Explosion
from Game_music import Game_Music
from Game_Status import Game_Status

setting = Settings()

hero_ship_x = 100
hero_ship_y = 100

hero_left = False
hero_right = False
hero_up = False
hero_down = False
hero_fire = False
press_count = 0

hero_bullets_group = pygame.sprite.Group()
enemy_hero_bullets_group = pygame.sprite.Group()

alien_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_1_group = pygame.sprite.Group()
enemy_2_group = pygame.sprite.Group()
enemy_3_group = pygame.sprite.Group()
hero_enemy_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

bolt_gold_group = pygame.sprite.Group()
shield_gold_group = pygame.sprite.Group()
big_rock_group = pygame.sprite.Group()
small_rock_group = pygame.sprite.Group()
recovery_group = pygame.sprite.Group()

explosion_group = pygame.sprite.Group()

start_generation_time = time.time()
start_enemy_hero_fire_space = time.time()
start_rock_generation_time = time.time()
start_recovery_generation_time = time.time()
start_time = datetime.now()
end_time = None

start_speed = 0.2
end_speed = 4

t_start = time.time()
h_start = time.time()

def render_bg(BG):
    BG.draw()
    BG.move()

def render_health(HEALTH):
    HEALTH.draw_health()

def render_time(times,time):
    t = str(time).split(':')
    # fill numbers by zero when the number less than 10
    times.draw_info("Time: %02s:%02s" % (t[1],
                                         t[2].split('.')[0]))

def render_scores(scores):
    scores.draw_info("SCORES: " + str(setting.scores))



def key_mouse_events(game_status):
    pygame.key.stop_text_input()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_scores()
            game_status.is_running = False
            setting.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
                game_status.is_pause = True
                game_status.is_running = False
                game_status.is_over = False
                game_status.is_start = False
            hero_status(event,'down')
        if event.type == pygame.KEYUP:
            hero_status(event,'up')

def hero_status(event,status):
    global hero_up,hero_down,hero_left,hero_right,hero_fire,press_count
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        if status == 'down':
            hero_up = True
        else:
            hero_up = False

    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        if status == 'down':
            hero_down = True
        else:
            hero_down = False

    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        if status == 'down':
            hero_left = True
        else:
            hero_left = False

    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        if status == 'down':
            hero_right = True
        else:
            hero_right = False

    if event.key == pygame.K_SPACE:
        press_count = 1
        if status == 'down':
            hero_fire = True
        else:
            hero_fire = False

def hero_action(screen,Hero_ship,hero_shoot):
    global press_count

    if hero_up and Hero_ship.y >= 0:
        Hero_ship.move_sprite(0,-setting.hero_speed_y)
    elif hero_down and Hero_ship.y <= setting.window_height - setting.hero_size[1]:
        Hero_ship.move_sprite(0,setting.hero_speed_y)
    elif hero_left and Hero_ship.x >= 0:
        Hero_ship.move_sprite(-setting.hero_speed_x,0)
    elif hero_right and Hero_ship.x <= setting.window_width - setting.hero_size[0]:
        Hero_ship.move_sprite(setting.hero_speed_x,0)

    if hero_fire and len(hero_bullets_group) < setting.hero_bullet_limit\
            and press_count == 1:
        bullet = Bullet(screen,Hero_ship.x + setting.hero_size[0],
                        Hero_ship.y + setting.hero_size[1] / 2 - 4,
                        setting.bullet_img_1_path)
        Hero_ship.shoot(bullet,hero_bullets_group)
        hero_shoot.music_action()
    # Continuous fired limit when press space
    # every press space only one bullet being fired
    press_count = 0

def add_scores(ship):
    setting.scores += ship.setting_life

def write_scores():
    if not os.path.isfile(setting.file_name):
        with open(setting.file_name,"w",encoding="utf-8") as fw:
            if setting.scores != 0:
                fw.write("Highest Scores: %s" % str(setting.scores))
    else:
        with open(setting.file_name,"r",encoding="utf-8") as fr:
            data = fr.read()
            if (not data and setting.scores != 0) or setting.scores > int(data.split(": ")[1]):
                with open(setting.file_name,"w",encoding="utf-8") as fw:
                    fw.write("Highest Scores: %s" % str(setting.scores))


def render_bullet():
    for b in hero_bullets_group:
        b.draw_bullet()
        b.move_bullet(setting.hero_bullet_speed,0)
        if b.x > setting.window_width or b.y < 0 or b.y > setting.window_height:
            hero_bullets_group.remove(b)

    for b1 in enemy_hero_bullets_group:
        b1.draw_bullet()
        b1.move_bullet(-setting.hero_bullet_speed,0)
        if b1.x < 0 or b1.y <0 or b1.y > setting.window_height:
            enemy_hero_bullets_group.remove(b1)

def generation_enemies(screen):
    global start_generation_time
    end_generation_time = time.time()

    if end_generation_time - start_generation_time >= setting.generation_space and \
        random.random() >= setting.alien_prob:
        start_generation_time = end_generation_time

        Alien = Ship(screen,setting.window_width + setting.alien_img_width,random.randint(10,setting.window_height - setting.alien_img_height),
                     setting.alien_img_path,setting.alien_life,"alien")
        alien_group.add(Alien)
        return

    if end_generation_time - start_generation_time >= setting.generation_space \
        and random.random() >= setting.enemy_prob:
        start_generation_time = end_generation_time
        Enemy = Ship(screen,setting.window_width + setting.enemy_img_width,random.randint(10,setting.window_height - setting.enemy_img_height)
                     ,setting.enemy_img_path,setting.enemy_life,"enemy")
        enemy_group.add(Enemy)
        return

    if end_generation_time - start_generation_time >= setting.generation_space \
        and random.random() >= setting.enemy_2_prob:
        start_generation_time = end_generation_time
        Enemy_2 = Ship(screen,setting.window_width + setting.enemy_2_img_width,random.randint(10,setting.window_height - setting.enemy_2_img_height),
                       setting.enemy_2_img_path,setting.enemy_2_life,"enemy_2")
        enemy_2_group.add(Enemy_2)
        return

    if end_generation_time - start_generation_time >= setting.generation_space \
        and random.random() <= setting.enemy_3_prob:
        start_generation_time = end_generation_time
        Enemy_3 = Ship(screen,setting.window_width + setting.enemy_3_img_width,random.randint(10,setting.window_height - setting.enemy_3_img_height),
                       setting.enemy_3_img_path,setting.enemy_3_life,"enemy_3")
        enemy_3_group.add(Enemy_3)
        return

    if end_generation_time - start_generation_time >= setting.generation_space \
        and random.random() <= setting.enemy_hero_prob:
        start_generation_time = end_generation_time
        Enemy_Hero = Enemy_Hero_Ship(screen,setting.window_width + setting.enemy_hero_img_width,random.randint(10,setting.window_height - setting.enemy_hero_img_height),
                               setting.enemy_hero_img_path,setting.hero_enemy_life,"enemy_hero")
        hero_enemy_group.add(Enemy_Hero)
        return

    if end_generation_time - start_generation_time >= setting.generation_space:
        start_generation_time = end_generation_time
        Enemy_1 = Ship(screen,setting.window_width + setting.enemy_1_img_width,random.randint(10,setting.window_height - setting.enemy_1_img_height),
                       setting.enemy_1_img_path,setting.enemy_1_life,"enemy_1")
        enemy_1_group.add(Enemy_1)
        return

def draw_enemies(screen,enemy_shoot):

    global start_enemy_hero_fire_space
    for a in alien_group:
        a.draw_sprite()
        a.move_sprite(-setting.alien_speed,0)
        if a.x < -setting.window_width / 2:
            alien_group.remove(a)

    for e in enemy_group:
        e.draw_sprite()
        e.move_sprite(-setting.enemy_speed,0)
        if e.x < -setting.window_width / 2:
            enemy_group.remove(e)

    for e1 in enemy_1_group:
        e1.draw_sprite()
        e1.move_sprite(-setting.enemy_1_speed,0)
        if e1.x < -setting.window_width / 2:
            enemy_1_group.remove(e1)

    for e2 in enemy_2_group:
        e2.draw_sprite()
        e2.move_sprite(-setting.enemy_2_speed,0)
        if e2.x < -setting.window_width / 2:
            enemy_2_group.remove(e2)

    for e3 in enemy_3_group:
        e3.draw_sprite()
        e3.move_sprite(-setting.enemy_3_speed,0)
        if e3.x < -setting.window_width / 2:
            enemy_3_group.remove(e3)

    end_enemy_hero_fire_space = time.time()
    for h_e in hero_enemy_group:
        h_e.draw_sprite()
        h_e.move_sprite(-setting.enemy_hero_speed,0)
        if h_e.x < -setting.window_width / 2:
            hero_enemy_group.remove(h_e)

        if end_enemy_hero_fire_space - start_enemy_hero_fire_space >= setting.enemy_hero_fire_space:
            start_enemy_hero_fire_space = end_enemy_hero_fire_space
            bullet = Bullet(screen,h_e.x + 10,h_e.y + setting.enemy_hero_img_width / 2 - 10,
                            setting.bullet_img_2_path)
            h_e.shoot(bullet,enemy_hero_bullets_group)
            enemy_shoot.music_action()

def reset_event_when_time_up():
    global t_start,h_start
    t_end = time.time()
    h_end = time.time()
    if t_end - t_start >= setting.event_space:
        t_start = t_end
        setting.generation_space -= 0.03
        setting.rock_generation_space -= 0.03
        setting.recovery_generation_space -= 0.02

    if h_end - h_start >= setting.hero_bullet_incr_time:
        h_start = h_end
        setting.hero_bullet_limit += setting.hero_bullet_incr


def generation_rock(screen):
    global start_rock_generation_time

    speed_x = start_speed + (end_speed - start_speed) * random.random()
    speed_y = start_speed + (end_speed - start_speed) * random.random()

    end_rock_generation_time = time.time()
    r1 = random.randint(1, 2)
    r2 = random.randint(1,2) #decided which ways the rock will go
    if r2 == 1:
        speed_x = speed_x
    else:
        speed_x = -speed_x

    if end_rock_generation_time - start_rock_generation_time >= setting.rock_generation_space \
            and random.random() <= setting.rock_big_prob:
        start_rock_generation_time = end_rock_generation_time
        Big_Rock = None

        if r1 == 1:
            Big_Rock = Universe_Stuff(screen,random.randint(100,setting.window_width - 100),
                                  -setting.rock_big_img_1_height - 10,setting.rock_big_imgs[0],2,0,
                                      -speed_x,speed_y,"big_rock")
        else:
            Big_Rock = Universe_Stuff(screen,random.randint(100,setting.window_width - 100),
                                  -setting.rock_big_img_2_height - 10,setting.rock_big_imgs[1],2,0,
                                      -speed_x,speed_y,"big_rock")
        big_rock_group.add(Big_Rock)
        return

    if end_rock_generation_time - start_rock_generation_time >= setting.rock_generation_space \
        and random.random() <= setting.rock_small_prob:
        start_rock_generation_time = end_rock_generation_time

        Small_Rock = None
        if r1 == 1:
            Small_Rock = Universe_Stuff(screen,random.randint(100,setting.window_width - 100)
                                        ,-setting.rock_small_img_1_height,setting.rock_small_imgs[0],1,
                                        0,-speed_x,speed_y,"small_rock")
        else:
            Small_Rock = Universe_Stuff(screen,random.randint(100,setting.window_width - 100),
                                        -setting.rock_small_img_2_height,setting.rock_small_imgs[1],1,
                                        0,-speed_x,speed_y,"small_rock")
        small_rock_group.add(Small_Rock)
        return

def generation_recovery_flush(screen):
    global start_recovery_generation_time
    speed_y = start_speed + (end_speed - start_speed) * random.random()

    end_recovery_generation_time = time.time()
    r2 = random.randint(0,1)
    if end_recovery_generation_time - start_recovery_generation_time >= setting.recovery_generation_space\
        and random.random() <= setting.recovery_generation_prob:
        start_recovery_generation_time = end_recovery_generation_time
        Recovery = None
        if r2 == 0:
            Recovery = Universe_Stuff(screen,random.randint(100,setting.window_width - 100),-setting.recovery_1_img_height - 10,
                                      setting.recovery_imgs[r2],0,1,0,speed_y,"recovery")
        else:
            Recovery = Universe_Stuff(screen,random.randint(100,setting.window_width - 100),
                                      -setting.recovery_2_img_height - 10,setting.recovery_imgs[r2],0,2,0,speed_y,
                                      "recovery")
        recovery_group.add(Recovery)


def draw_universe_stuff():
    for big_rock in big_rock_group:
        big_rock.draw()
        big_rock.move()
        if big_rock.x < -100 or big_rock.y > setting.window_height + 100:
            big_rock_group.remove(big_rock)

    for small_rock in small_rock_group:
        small_rock.draw()
        small_rock.move()
        if small_rock.x < -100 or small_rock.y > setting.window_height + 100:
            small_rock_group.remove(small_rock)

    for recovery in recovery_group:
        recovery.draw()
        recovery.move()
        if recovery.y > setting.window_height + 100:
            recovery_group.remove(recovery)



def collision_with(screen,group_1,group_2,exec_func,
                   bomb,hero_fire,rocket):
    for g1 in group_1:
        for g2 in group_2:
            if (g1.x > g2.x and g1.x < g2.x + g2.width) and (g1.y >
            g2.y and g1.y < g2.y + g2.height):
                exec_func(screen,group_1,group_2,g1,g2,bomb,hero_fire,rocket)
                return

def bullet_with_enemies_ship(screen,bullet_group,ship_group,bullet,ship,
                             bomb,hero_fire,rocket):
    bullet_group.remove(bullet)
    ship.life -= 1
    hero_fire.music_action()
    if ship.life <= 0:
        explosion = Explosion(screen, ship.x,
                              ship.y, setting.explosion_images)
        explosion_group.add(explosion)
        add_scores(ship)
        bomb.music_action()
        ship_group.remove(ship)


def rock_with_enemies_ship(screen,rock_group,ship_group,rock,ship
                           ,bomb,hero_fire,rocket):
    ship.life -= rock.attack
    rocket.music_action()
    rock_group.remove(rock)
    if ship.life <= 0:
        explosion = Explosion(screen,ship.x,
                              ship.y,setting.explosion_images)
        explosion_group.add(explosion)
        bomb.music_action()
        ship_group.remove(ship)


def recovery_hero_life(hero,recovery_group,HEALTH,recovery_life):
    for recovery in recovery_group:
        if (recovery.x > hero.x and recovery.x < hero.x + hero.width) and \
                (recovery.y > hero.y and recovery.y < hero.y + hero.height):
                if HEALTH.hero_life < setting.hero_life:
                    HEALTH.hero_life += recovery.recovery_life
                    if HEALTH.hero_life > 10:
                        HEALTH.hero_life -= HEALTH.hero_life - setting.hero_life
                    recovery_life.music_action()
                    recovery_group.remove(recovery)
                    return

def draw_explosion_when_time_up():
    for b in explosion_group:
        if b.explosion_finish:
            explosion_group.remove(b)
            return
        b.explosion_animation()

# when hero get hurt
def hero_damage(hero,enemies_group,HEALTH,hero_damage_func,screen,
                bomb,Game_status,fall):
    for enemy in enemies_group:
        if hero.x >= enemy.x and hero.x <= enemy.x + enemy.width - 10 \
            and hero.y >= enemy.y and hero.y <= enemy.y + enemy.height - 10:
            hero_damage_func(screen,hero,enemy,HEALTH,bomb,Game_status,fall)
            return
        if enemy.x >= hero.x and enemy.x <= hero.x + hero.width - 10 \
                and enemy.y >= hero.y and enemy.y <= hero.y + hero.height - 10:
            hero_damage_func(screen,hero, enemy, HEALTH,bomb,Game_status,fall)
            return

def hero_with_enemies(screen,hero,enemy,HEALTH,bomb,Game_status,fall):
    if enemy.name == "alien":
        HEALTH.hero_life -= 1
        alien_group.remove(enemy)
    elif enemy.name == "enemy":
        HEALTH.hero_life -= 1
        enemy_group.remove(enemy)
    elif enemy.name == "enemy_1":
        HEALTH.hero_life -= 1
        enemy_1_group.remove(enemy)
    elif enemy.name == "enemy_2":
        HEALTH.hero_life -= 2
        enemy_2_group.remove(enemy)
    elif enemy.name == "enemy_3":
        HEALTH.hero_life -= 5
        enemy_3_group.remove(enemy)
    explosion = Explosion(screen,enemy.x,enemy.y,setting.explosion_images)
    explosion_group.add(explosion)
    bomb.music_action()

    if HEALTH.hero_life <= 0:
        Game_status.is_over = True
        Game_status.is_start = False
        Game_status.is_pause = False
        Game_status.is_running = False
        draw_explosion_when_time_up()
        fall.music_action()
        return
def hero_with_enemy_bullet(screen,hero,bullet,HEALTH,bomb,Game_status,fall):
    HEALTH.hero_life -= 1
    enemy_hero_bullets_group.remove(bullet)

    if HEALTH.hero_life <= 0:
        Game_status.is_over = True
        Game_status.is_start = False
        Game_status.is_running = False
        Game_status.is_pause = False
        draw_explosion_when_time_up()
        fall.music_action()
        return

def hero_with_rock(screen,hero,rock,HEALTH,bomb,Game_status,fall):
    HEALTH.hero_life -= rock.attack
    if rock.name == "big_rock":
        big_rock_group.remove(rock)
    elif rock.name == "small_rock":
        small_rock_group.remove(rock)

    explosion = Explosion(screen,rock.x,rock.y,setting.explosion_images)
    explosion_group.add(explosion)
    bomb.music_action()

    if HEALTH.hero_life <= 0:
        Game_status.is_over = True
        Game_status.is_start = False
        Game_status.is_running = False
        Game_status.is_pause = False
        draw_explosion_when_time_up()
        fall.music_action()
        return

def game_logical(screen,Game_status,BG1,getready,clock,start_music,background_music,fall_music,pause_moment):
    global start_time
    HEALTH = Health(screen)
    scores = Game_Info(screen, setting.scores_size, setting.scores_color,
                       screen.get_width() / 2.5, 10)
    times = Game_Info(screen, setting.t_font_size, setting.t_font_color,
                      screen.get_width() - 200, 10)
    Hero_ship = Hero_Ship(screen, hero_ship_x, hero_ship_y, setting.hero_img_path,
                          setting.hero_life, "hero")
    hero_group.add(Hero_ship)
    bomb = Game_Music(setting.bomb)
    enemy_shoot = Game_Music(setting.enemy_shoot_volume)
    hero_shoot = Game_Music(setting.hero_shoot_volume)
    fall = Game_Music(setting.fall)
    rocket = Game_Music(setting.rocket)
    recovery_life = Game_Music(setting.recovery_life)
    is_pass_pause_time = False

    reset_start_time()
    while Game_status.is_running:
        key_mouse_events(Game_status)
        end_time = datetime.now()
        diff_time = end_time - start_time

        # render your game action here
        render_bg(BG1)

        if is_pass_pause_time:
            start_music.action = "stop"
            start_music.music_action()
            pause_moment.action = "stop"
            pause_moment.music_action()
            fall_music.action = "stop"
            fall_music.music_action()
            background_music.action = "play"
            background_music.music_action()
            is_pass_pause_time = False

        Hero_ship.draw_sprite()
        hero_action(screen, Hero_ship, hero_shoot)

        generation_enemies(screen)
        draw_enemies(screen, enemy_shoot)

        generation_rock(screen)
        generation_recovery_flush(screen)

        draw_universe_stuff()

        render_scores(scores)

        render_time(times,diff_time)

        render_health(HEALTH)
        render_bullet()

        # check if the hero bullet collision with enemy
        collision_with(screen, hero_bullets_group, alien_group, bullet_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, hero_bullets_group, enemy_group, bullet_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, hero_bullets_group, enemy_1_group, bullet_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, hero_bullets_group, enemy_2_group, bullet_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, hero_bullets_group, enemy_3_group, bullet_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, hero_bullets_group, hero_enemy_group, bullet_with_enemies_ship, bomb, hero_shoot,
                       rocket)

        # check if the rock collision with enemy
        collision_with(screen, big_rock_group, alien_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, big_rock_group, enemy_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, big_rock_group, enemy_1_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, big_rock_group, enemy_2_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, big_rock_group, enemy_3_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, big_rock_group, hero_enemy_group, rock_with_enemies_ship, bomb, hero_shoot,
                       rocket)

        collision_with(screen, small_rock_group, alien_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, small_rock_group, enemy_group, rock_with_enemies_ship, bomb, hero_shoot, rocket)
        collision_with(screen, small_rock_group, enemy_1_group, rock_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, small_rock_group, enemy_2_group, rock_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, small_rock_group, enemy_3_group, rock_with_enemies_ship, bomb, hero_shoot,
                       rocket)
        collision_with(screen, small_rock_group, hero_enemy_group, rock_with_enemies_ship, bomb, hero_shoot,
                       rocket)

        # recovery the life of hero
        recovery_hero_life(Hero_ship, recovery_group, HEALTH, recovery_life)
        reset_event_when_time_up()
        draw_explosion_when_time_up()

        hero_damage(Hero_ship, alien_group, HEALTH, hero_with_enemies, screen, bomb,Game_status,fall)
        hero_damage(Hero_ship, enemy_group, HEALTH, hero_with_enemies, screen, bomb,Game_status,fall)
        hero_damage(Hero_ship, enemy_1_group, HEALTH, hero_with_enemies, screen, bomb,Game_status,fall)
        hero_damage(Hero_ship, enemy_2_group, HEALTH, hero_with_enemies, screen, bomb,Game_status,fall)
        hero_damage(Hero_ship, enemy_3_group, HEALTH, hero_with_enemies, screen, bomb,Game_status,fall)

        hero_damage(Hero_ship, enemy_hero_bullets_group, HEALTH, hero_with_enemy_bullet, screen, bomb,Game_status,fall)

        hero_damage(Hero_ship, big_rock_group, HEALTH, hero_with_rock, screen, bomb,Game_status,fall)
        hero_damage(Hero_ship, small_rock_group, HEALTH, hero_with_rock, screen, bomb,Game_status,fall)

        if Game_status.is_pause:
            is_pass_pause_time = True
            start_music.action = "stop"
            start_music.music_action()
            background_music.action = "stop"
            background_music.music_action()
            fall_music.action = "stop"
            fall_music.music_action()
            pause_moment.action = "play"
            pause_moment.music_action()

            pause_time_1 = datetime.now()
            Game_status.game_status(BG1, getready, start_music, background_music, fall_music, pause_moment)
            pause_time_2 = datetime.now()
            start_time = start_time + (pause_time_2 - pause_time_1)
            reset_start_time()


        pygame.display.flip()
        clock.tick(setting.game_fps)


def reset_stuff_to_init():
    global hero_left,hero_right,hero_up,hero_down,hero_fire,press_count,\
    start_time

    hero_left = False
    hero_right = False
    hero_up = False
    hero_down = False
    hero_fire = False
    press_count = 0

    alien_group.empty()
    enemy_group.empty()
    enemy_1_group.empty()
    enemy_2_group.empty()
    enemy_3_group.empty()
    hero_enemy_group.empty()
    hero_bullets_group.empty()
    enemy_hero_bullets_group.empty()
    big_rock_group.empty()
    small_rock_group.empty()
    recovery_group.empty()
    hero_group.empty()
    explosion_group.empty()
    bolt_gold_group.empty()
    shield_gold_group.empty()
    start_time = datetime.now()
    reset_start_time()
    write_scores()
    setting.scores = 0
    setting.hero_bullet_limit = 3

def reset_start_time():
    global start_generation_time, start_rock_generation_time, \
    start_recovery_generation_time, t_start, h_start,start_time
    start_generation_time = time.time()
    start_rock_generation_time = time.time()
    start_recovery_generation_time = time.time()
    t_start = time.time()
    h_start = time.time()

def game_run(screen,clock):
    global start_generation_time,start_rock_generation_time,\
    start_recovery_generation_time,t_start,h_start,start_time

    getready = Game_Music(setting.get_ready)
    Game_status = Game_Status(screen)

    background_music = Game_Music(setting.background_music)
    start_music = Game_Music(setting.start_music)
    fall_music = Game_Music(setting.fall_music)
    pause_moment = Game_Music(setting.pause_moment)

    background_music.is_repeat = True
    start_music.is_repeat = True
    fall_music.is_repeat = True
    pause_moment.is_repeat = True


    while setting.running:
        BG1 = Background(screen)

        if Game_status.is_start:
            reset_start_time()
            start_music.action = "play"
            start_music.music_action()
            background_music.action = "stop"
            background_music.music_action()
            pause_moment.action = "stop"
            pause_moment.music_action()
            fall_music.action = "stop"
            fall_music.music_action()
            Game_status.game_status(BG1, getready, start_music, background_music, fall_music, pause_moment)

        if Game_status.is_running:
            reset_start_time()
            background_music.action = "play"
            background_music.music_action()
            start_music.action = "stop"
            start_music.music_action()
            pause_moment.action = "stop"
            pause_moment.music_action()
            fall_music.action = "stop"
            fall_music.music_action()
            game_logical(screen,Game_status,BG1,getready,clock,start_music,background_music,fall_music,pause_moment)

        if Game_status.is_over:
            reset_start_time()
            start_music.action = "stop"
            start_music.music_action()
            background_music.action = "stop"
            background_music.music_action()
            pause_moment.action = "stop"
            pause_moment.music_action()
            fall_music.action = "play"
            fall_music.music_action()
            Game_status.game_status(BG1, getready, start_music, background_music, fall_music, pause_moment)
            reset_stuff_to_init()

        Game_status.game_status(BG1,getready,start_music,background_music,fall_music,pause_moment)



