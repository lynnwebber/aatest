handle_open = fn
    {:ok,file} -> "First Line: #{IO.read(file,:line)}"
    {_,error} -> "Error: #{:file.format_error(error)}"
end
IO.puts handle_open.(File.open("/Users/lynn/Desktop/rtu_channel_work.xml"))
IO.puts handle_open.(File.open("whoknows.txt"))

fb = fn
    0, 0, _ -> "FizzBuzz"
    0, _, _ -> "Fizz"
    _, 0, _ -> "Buzz"
    _, _, a -> a
end

xtest = fn
    n -> fb.(rem(n,3),rem(n,5),n)
end

IO.puts xtest.(10)
IO.puts xtest.(11)
IO.puts xtest.(12)
IO.puts xtest.(13)
IO.puts xtest.(14)
IO.puts xtest.(15)
IO.puts xtest.(16)
IO.puts xtest.(17)

