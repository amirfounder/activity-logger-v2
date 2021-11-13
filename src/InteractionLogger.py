from datetime import datetime
import os


class InteractionLogger:
  
  _root_log_directory = 'C:\\x\\logs\\interaction-logger'
  _prev_log_today = None

  _kill_logger = False
  _kill_key_one_pressed = False
  _kill_key_two_pressed = False

  _max_log_file_size = 50 * 1000 * 1000

  _mouse_click_event_abbreviation = 'mc'
  _mouse_move_event_abbreviation = 'mm'
  _mouse_scoll_event_abbreviation = 'ms'
  _key_press_event_abbreviation = 'kp'
  _key_release_event_abbreviation = 'kr'

  def run():
    pass

  def log_event(self, version='1'):
    pass

  def build_log_file():
    today = datetime.now().strftime(r'%Y_%m_%d')

  def get_today():
    return datetime.now().strftime(r'%Y_%m_%d')

  def get_timestamp():
    return datetime.now().strftime(r'%H_%M_%S_%f')