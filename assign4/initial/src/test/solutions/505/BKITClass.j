.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
	bipush 10
	putstatic BKITClass/a I
	ldc "string"
	putstatic BKITClass/b Ljava/lang/String;
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "last of us"
	astore_1
	aload_1
	invokestatic BKITClass/f(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static f(Ljava/lang/String;)Ljava/lang/String;
.var 0 is x Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LBKITClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
