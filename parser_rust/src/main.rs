extern crate serde_json;
extern crate serde;
extern crate serde_stacker;

use serde::de::Deserialize;
use serde_json::{Deserializer, Value};

fn main() {
    let mut d = Deserializer::from_reader(std::io::stdin());
    d.disable_recursion_limit();
    let d = serde_stacker::Deserializer::new(&mut d);
    let v: Value = Value::deserialize(d).unwrap();
    print_value(&v);

    carefully_drop_nested_arrays(v);
}

fn print_value(mut v: &Value) {
    let mut level = 0;
    let mut stack = vec![value];
    while let Some(value) = stack.pop() {
        match value {
            Value::Array(array) => {
                if array.len() > 1 {
                    unimplemented!()
                }
                level += 1;
                stack.extend(array);
            }
            _ => unimplemented!(),
        }
    }
    for _ in 0..level {
        print!("[");
    }
    for _ in 0..level {
        print!("]");
    }
    println!();
}

fn carefully_drop_nested_arrays(value: Value) {
    let mut stack = vec![value];
    while let Some(value) = stack.pop() {
        if let Value::Array(array) = value {
            stack.extend(array);
        }
    }
}
