handle_open = fn
    {:ok,file} -> "First Line: #{IO.read(file,:line)}"
    {_,error} -> "Error: #{:file.format_error(error)}"
end
IO.puts handle_open.(File.open("/Users/lynn/Desktop/time_tracker.txt"))
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

ytest = &(fb.(rem(&1,3),rem(&1,5),&1))

IO.puts ytest.(10)
IO.puts ytest.(12)
IO.puts xtest.(14)
IO.puts xtest.(15)
IO.puts xtest.(17)

IO.puts Enum.each [1,2,3,4], &(IO.inspect(&1))
