#!/usr/bin/env python
# Advent Of Code 2025 Day 2 by Craig Brennan
# https://adventofcode.com/2025/day/2

# Save ranges from file
with open('input/day02_input.txt') as f:
   max_len = 0
   id_ranges = []
   for range_str in f.read().strip().split(','):
      a, b = range_str.split('-')
      id_ranges.append([a,b])
      if len(b) > max_len:
         max_len = len(b)

invalid_total = 0

def find_invalid(a: str, b: str):
   invalid = []

   for i in range(int(a), int(b)+1):
      n = str(i)
      if len(n)%2 != 0:
         continue
      if n[0:len(n)//2] == n[len(n)//2:]:
         invalid.append(int(n))

   return invalid

for id_range in id_ranges:
   for x in find_invalid(*id_range):
      invalid_total += x

print(f'Part 1: {invalid_total}')