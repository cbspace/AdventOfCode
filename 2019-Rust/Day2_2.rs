use std::fs;

fn main() {
    // Read data from file into vector
    let data = fs::read_to_string("./input.txt").unwrap();
    let s = data.trim();
    let mem_initial: Vec<i32> = s.split(',').map(|s| s.parse().unwrap()).collect();

    let mut noun = 0;
    let mut verb = 0;
    let mut done = false;

    while noun < 100 && !done {
        while verb < 100 && !done {
            if check_inputs(&mem_initial, noun, verb) == 19690720 {
                done = true;
                println!("{}",100 * noun + verb);
            }      
            verb += 1;
        }
        verb = 0;
        noun += 1;
    }
}

fn check_inputs(mem_initial: &Vec<i32>, noun: i32, verb: i32) -> i32 {
    let mut mem = mem_initial.clone();

    // Correct corrupted data
    mem[1] = noun;
    mem[2] = verb;

    let mut pc = 0;

    // Start the computer
    while pc < mem.len() {
        let v1 = mem[pc+1] as usize;
        let v2 = mem[pc+2] as usize;
        let v3 = mem[pc+3] as usize;
        if !(v1 < mem.len() && v2 < mem.len()) {break;}
        match mem[pc] {
            1 => {
                if v3 < mem.len() {
                    mem[v3] = mem[v1] + mem[v2];
                }
            },
            2 => {
                if v3 < mem.len() {
                    mem[v3] = mem[v1] * mem[v2];
                }
            },
            99 => break,
            _ => println!("Invalid instruction: {}",mem[pc])
        }
        pc += 4;
    }
    return mem[0];
}
