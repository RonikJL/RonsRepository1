public class StrCompression{
    public static void main(String[] args){
        char []chars=new char[] {'a','a','b','b','c','c','c'};
        int x=compress(chars);
        System.out.println(x);
        System.out.println(chars);
    }
    public static int compress(char[] chars) {
        int firstElement = 0, secondElement = 0;
        while(firstElement < chars.length) {
            char c = chars[firstElement];
            chars[secondElement++] = c;
            int count = firstElement;
            while (firstElement + 1 < chars.length && chars[firstElement+1] == chars[firstElement]) {
                firstElement++;
            }
            count = firstElement - count + 1;
            if (count > 1) {
                for ( char c1 : String.valueOf(count).toCharArray()) {
                    chars[secondElement++] = c1;
                }
            }
            firstElement++;
        }
        return secondElement;
    }
}
