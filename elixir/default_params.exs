defmodule Example1 do
  def testone(p1, p2 \\ 2, p3 \\ 3, p4) do
    IO.inspect [p1,p2,p3,p4]
  end
end

defmodule Example2 do
  def testtwo(p1,p2\\2)
  def testtwo(p1,p2) when is_list(p1) do
    "a list is what was passed in #{p1} and #{p2}"
  end
  def testtwo(p1,p2) do
    "Here is what was passed in #{p1} and #{p2}"
  end
end
