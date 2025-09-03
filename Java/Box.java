public class Box<T> {
    private T value;

    public void SetValue(T newValue)
    {
        this.value = newValue;
    }

    public T GetValue()
    {
        return this.value;
    }

    public void Printvalue()
    {
        System.out.println(this.value);
    }
}
