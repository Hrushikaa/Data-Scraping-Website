<?php

$name = $_POST['name'];
$visitor_email = $_POST['email'];
$subject = $_POST['subject'];
$feedback = $_POST['feedback'];

$email_from = 'info@something.com';
$email_subject = 'New Feedback first trends';
$email_body = 'Username: $name.\n'.
                'user email: $visitor_email.\n'.
                 'subject: $subject.\n'.
                 'feedback: $feedback.\n';

$to = 'hrushikam5@gmail.com';

$headers = "From $email_from \r\n";
$headers . ="Reply-to: $visitor_email \r\n";

mail($to, $email_subject, $email_body, $headers);

header('Location: feedbk.html');

?>