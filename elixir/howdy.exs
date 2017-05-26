# the first test of elixir.  looking forward...
IO.puts "howdy world\nhere comes some cowboy coding"
IO.puts "lets check out some first class function stuff:"
add_one = fn a -> a + 1 end

IO.puts add_one.(8)

# do some pattern matching and learn about case/do/end
