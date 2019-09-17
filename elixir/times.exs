defmodule Times do
  def double(n), do: n * 2
  def tripple(n), do: n * 3
end

defmodule Guard do
  def what_is(x) when is_number(x) do
    IO.puts "#{x} is a number"
  end
  def what_is(x) when is_list(x) do
    IO.puts "#{inspect(x)} is a list"
  end
  def what_is(x) when is_atom(x) do
    IO.puts "#{x} is an an atom"
  end
end

