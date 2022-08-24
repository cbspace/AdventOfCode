use std::fs;

fn main() {
    // Read data from file into vector
    let data = fs::read_to_string("./input.txt").unwrap();
    let s = data.trim();
    let mut mem: Vec<i32> = s.split(',').map(|s| s.parse().unwrap()).collect();

    // Correct corrupted data
    mem[1] = 12;
    mem[2] = 2;

    let mut pc = 0;

    // Start the computer
    loop {
        let v1 = mem[pc+1] as usize;
        let v2 = mem[pc+2] as usize;
        let v3 = mem[pc+3] as usize;
        match mem[pc] {
            1 => {
                mem[v3] = mem[v1] + mem[v2];
            },
            2 => {
                mem[v3] = mem[v1] * mem[v2];
            },
            99 => break,
            _ => println!("Invalid instruction: {}",mem[pc])
        }
        pc += 4;
    }
    println!("{}",mem[0]);
}
