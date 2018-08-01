from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class SignupModelForm(forms.ModelForm):
    pass


class SignupForm(forms.Form):
    """
    회원가입을 작성하는 form(회원가입 화면 형태)
    """
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'style': 'margin-bottom: 30px;',
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    gender = forms.CharField(
        label='성별',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
            choices=User.CHOICE_GENDER,
        )
    )

    introduce = forms.CharField(
        label='소개',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )

    def clean_username(self):
        """
        사용자가 입력한 username이 기존 User의 username과 일치하는 것이 있는지 확인하는 함수
        :return:
        """
        # username field의 clean()실행 결과가 self.cleaned_data['username']에 있음
        # 회원가입을 하려는 사용자가 적은 username 값이 data 변수에 할당된다.
        data = self.cleaned_data['username']
        # 이미 사용중인 id가 있는지를 확인해준다.
        if User.objects.filter(username=data).exists():
            # username과 data값이 일치하는 것이 존재하면 ValidationError 를 일으킴
            raise ValidationError('이미 사용중인 아이디입니다')

        return data

    def clean(self):
        """
        사용자가 입력한 password, password2가 서로 일치하는지 확인해주는 함수
        :return:
        """
        # is_valid()가 실행되면서 사용자로부터 폼에서 입력받은
        # {'password': '입력값', 'password2':'입력값'}이 cleaned_data 에 삽입된다.
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            self.add_error('password2', '비밀번호와 비밀번호확인의 값이 일치하지 않습니다')
        return self.cleaned_data

    def signup(self):
        """
        새로운 user 를 생성하는 함수
        :return:
        """
        fields = [
            'username',
            'email',
            'password',
            'gender',
            'introduce',
        ]
        # cleaned_data에 입력된 값이 각각의 key, value에 들어가는데
        # 이때 key의 값이 fields안에 들어있다면 해당 key값에 들어가는 사용자 값이 value에 들어간다.
        # 아래 예시를 보면 조금더 이해가 잘 갈 듯 싶다..
        create_user_dict = {key: value for key, value in self.cleaned_data.items() if key in fields}

        # create_user_dict = {}
        # for key, value in self.cleaned_data.items():
        #     if key in fields:
        #         create_user_dict[key] = value

        # 위에서 만들어낸 user_dict 를 가지고 user 를 만든다.
        user = User.objects.create_user(**create_user_dict)

        return user
