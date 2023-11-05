import { useMutation, gql } from "@apollo/client";

const REPLY = gql`
mutation CreateUser($id: ID!, $name: String!, $username: String!, $password: String!, $email: String!, $admin: Boolean!, $phone_number: Int!, $ad: String!) {
  createUser(id: $id, name: $name, username: $username, password: $password, email: $email, admin: $admin, phone_number: $phone_number, ad: $ad) {
    id
    name
    username
    password
    email
    admin
    phone_number
    ad
  }
}
`;

export default function useCreateUserMutation() {
  return useMutation(REPLY);
}
