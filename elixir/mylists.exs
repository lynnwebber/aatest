defmodule MyList do
  def len([]) do 0 end
  def len([_|tail]) do
    1 + len(tail)
  end

  def square([]) do [] end
  def square([head|tail]) do
    [head*head|square(tail)]
  end

  def map([],_func) do [] end
  def map([head|tail],func) do
    [func.(head) | map(tail,func)]
  end

  def sum([],tot) do tot end
  def sum([head|tail],tot) do
    sum(tail, head+tot)
  end

  def reduce([], rv, _) do rv end
  def reduce([head|tail], rv, func) do
    IO.puts rv
    reduce(tail, func.(head, rv), func)
  end

  # max external function 
  def max(lst) do _max(lst,0) end
  # private functions
  defp _max([],hival) do hival end
  defp _max([head|tail],hival) when head >= hival do
    hival = head
    _max(tail,hival)
  end
  defp _max([head|tail],hival) do
    _max(tail,hival)
  end

end


