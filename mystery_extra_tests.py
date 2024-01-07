from tms_mystery import solve
#from mystery import solve

story_lines = [
  ('Ed Puckett', 'means', True, 0.5),
  ('Ed Puckett', 'opportunity', True, 0.8),
  ('Ed Puckett', 'motive', False, 0.8),
  ('Louis Murphy', 'means', False, 1.0),
  ('Louis Murphy', 'opportunity', False, 1.0),
  ('Louis Murphy', 'motive', False, 1.0),
  ('Gene Roberts', 'means', True, 0.5),
  ('Gene Roberts', 'opportunity', True, 0.5),
  ('Gene Roberts', 'motive', False, 0.8),
  ('Justin Tanner', 'means', True, 0.5),
  ('Justin Tanner', 'opportunity', True, 0.9),
  ('Justin Tanner', 'motive', False, 0.8),
  ('George Whitley', 'means', True, 0.5),
  ('George Whitley', 'opportunity', True, 0.5),
  ('George Whitley', 'motive', False, 0.8)
]

assert 'Justin Tanner' == solve(story_lines)

story_lines = [
    ('A', 'motive', True, 0.8),
    ('A', 'means', True, 0.8),
    ('A', 'opportunity', True, 0.7),
    ('B', 'motive', True, 0.71),
    ('B', 'means', True, 0.8),
    ('B', 'opportunity', True, 0.7)
]

assert 'A' == solve(story_lines)
