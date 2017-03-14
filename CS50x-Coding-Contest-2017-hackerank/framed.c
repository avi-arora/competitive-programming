#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
  char *input = "this is a test string."; 
  int max_word_len = 0;
  int temp = 0;
  for (int i = 0; input[i] != '\0'; ++i)
  {
    
    temp++;
    if (input[i] == ' ')
    {
      temp--;
      if (temp > max_word_len)
      {
        max_word_len = temp;
      }
      temp = 0;
    }
  }
  if (temp > max_word_len)
  {
    max_word_len = temp;
  }
  int word_count = 1;
  temp = 0;
  while(input[temp] != '\0')
  {
    if (input[temp] == ' ')
    {
      word_count++;
    }
    temp++;
  }
  for (int i = 0; i < max_word_len + 4; ++i)
  {
    printf("#");
  }
  printf("\n");
  temp = 0;
  int p;
  for (int i = 0; i < word_count; ++i)
  {
    p = 1;
    printf("# ");
    while(input[temp] != '\0')
    {
      
      if (input[temp] == ' ')
      {
        temp++;
        break;
      }
      printf("%c", input[temp]);
      temp++;p++;
    }
    for(; p < max_word_len + 2;p++)
    {
      printf(" ");
    }
    printf("#\n");
  }
  for (int i = 0; i < max_word_len + 4; ++i)
  {
    printf("#");
  }
  printf("\n");

  return 0;
}