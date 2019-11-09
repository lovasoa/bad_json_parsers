defmodule ParserElixir do
  def main(_argv) do
    IO.binread(:all) |> Jason.decode! 
  end
end
